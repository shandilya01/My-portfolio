from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    job_obj = Job.objects
    return render(request, 'jobs/home.html' , {'jobs':job_obj});
