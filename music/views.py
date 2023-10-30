from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .mocked_data import albums

# Create your views here.
def about(request):
    return HttpResponse('This site brings you all the information about music')


def guide(request):
    return render(request, template_name='guide.html', context={'app_name': 'music'})


def get_guide_album(request):
    data = albums.get_albums()
    return JsonResponse(data, safe=False)