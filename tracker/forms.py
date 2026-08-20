from django import forms
from .models import JobApplication, Interview, Category


class JobApplicationForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = JobApplication
        fields = [
            'job_title', 
            'company_name', 
            'location', 
            'salary', 
            'job_url', 
            'status', 
            'job_description', 
            'notes', 
            'categories'
        ]
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'job_url': forms.URLInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['interview_date', 'interview_type', 'notes']
        widgets = {
            'interview_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'interview_type': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }