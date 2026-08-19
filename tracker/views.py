from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import JobApplication, Interview
from .forms import JobApplicationForm, InterviewForm
from .services import analyze_job_description

@login_required
def dashboard(request):
    user_jobs = JobApplication.objects.filter(user=request.user)
    total_applications = user_jobs.count()
    status_counts = user_jobs.values('status').annotate(total=Count('status'))
    recent_applications = user_jobs.order_by('-application_date')[:5]
    upcoming_interviews = Interview.objects.filter(job_application__user=request.user).order_by('interview_date')[:5]

    context = {
        'total_applications': total_applications,
        'status_counts': status_counts,
        'recent_applications': recent_applications,
        'upcoming_interviews': upcoming_interviews,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def application_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    
    applications = JobApplication.objects.filter(user=request.user)
    
    if query:
        applications = applications.filter(Q(job_title__icontains=query) | Q(company_name__icontains=query))
    if status_filter:
        applications = applications.filter(status=status_filter)
        
    return render(request, 'tracker/application_list.html', {'applications': applications})

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
    return render(request, 'tracker/application_form.html', {'form': form})

@login_required
def ai_analysis(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    analysis = analyze_job_description(application.job_description)
    return render(request, 'tracker/ai_analysis.html', {'application': application, 'analysis': analysis})