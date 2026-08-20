from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import JobApplication, Interview
from .forms import JobApplicationForm, InterviewForm
from .services import analyze_job_description


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    user_jobs = JobApplication.objects.filter(user=request.user)
    upcoming_interviews = Interview.objects.filter(
        job_application__user=request.user
    ).select_related('job_application').order_by('interview_date')

    context = {
        'total_applications': user_jobs.count(),
        'wishlist_count': user_jobs.filter(status='Wishlist').count(),
        'applied_count': user_jobs.filter(status='Applied').count(),
        'interview_count': user_jobs.filter(status='Interview').count(),
        'offer_count': user_jobs.filter(status='Offer').count(),
        'rejected_count': user_jobs.filter(status='Rejected').count(),
        'recent_jobs': user_jobs.order_by('-application_date')[:5],
        'upcoming_interviews': upcoming_interviews,
    }
    return render(request, 'tracker/dashboard.html', context)


from .models import JobApplication, Interview, Category 

@login_required
def application_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    location_filter = request.GET.get('location', '')
    category_filter = request.GET.get('category', '')

    applications = JobApplication.objects.filter(user=request.user)

    if query:
        applications = applications.filter(
            Q(job_title__icontains=query) | 
            Q(company_name__icontains=query) |
            Q(location__icontains=query)
        )
    if status_filter:
        applications = applications.filter(status=status_filter)
    if location_filter:
        applications = applications.filter(location__icontains=location_filter)
    if category_filter:
        applications = applications.filter(categories__id=category_filter)

    categories = Category.objects.all()

    return render(request, 'tracker/application_list.html', {
        'applications': applications.distinct(),
        'categories': categories,
        'query': query,
        'status_filter': status_filter,
        'location_filter': location_filter,
        'category_filter': category_filter,
    })


@login_required
def create_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            form.save_m2m()
            return redirect('application_list')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/application_form.html', {'form': form, 'title': 'Add New Job Application'})


@login_required
def update_application(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'tracker/application_form.html', {'form': form, 'title': 'Edit Job Application'})


@login_required
def delete_application(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('application_list')
    return render(request, 'tracker/application_confirm_delete.html', {'job': job})


@login_required
def add_interview(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.job_application = job
            interview.save()
            job.status = 'Interview'
            job.save()
            return redirect('application_list')
    else:
        form = InterviewForm()
    return render(request, 'tracker/interview_form.html', {'form': form, 'job': job})


@login_required
def ai_analysis(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    analysis_result = analyze_job_description(job.job_description)
    return render(request, 'tracker/ai_analysis.html', {'job': job, 'analysis': analysis_result})