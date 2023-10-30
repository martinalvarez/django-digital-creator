from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse('This site brings you all the information about music')


def guide(request):
    return render(request, template_name='guide.html', context={'app_name': 'music'})

