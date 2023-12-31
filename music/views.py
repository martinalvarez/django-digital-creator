from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mocked_data import albums
from .models import Album, Artist

# Create your views here.
def about(request):
    return HttpResponse('This site brings you all the information about music')


def get_albums(request):
    try:
        albums = Album.objects.all()
        data = []
        for album in albums:
            data.append({
                'id': album.id,
                'image_url': album.image_url,                
                'name': album.name,
                'release': album.release
            })
        return JsonResponse(data, safe=False)        
    except Exception as error:
        return HttpResponseServerError("DB error")

@api_view()
def albums_list(request):
    return Response('coming soon')


def get_artists(request):
    try:
        artists = Artist.objects.all()
        data = [{'id': artist.id, 'name': artist.name } for artist in artists]
        return JsonResponse(data, safe=False)
    except Exception as error:
        return HttpResponseServerError("DB error")


def guide(request):
    return render(request, template_name='guide.html', context={'app_name': 'music'})


def get_guide_album(request):
    data = albums.get_albums()
    return JsonResponse(data, safe=False)