from django.http import HttpResponse
from datetime import datetime

def copyright(request):
    year = datetime.now().year
    return HttpResponse(f'Copyright {year}')