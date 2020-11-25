from django.shortcuts import render
# Create your views here.
def jobsposting(request):
    return render(request, 'Jobsapp/index.html')