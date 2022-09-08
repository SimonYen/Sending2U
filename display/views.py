from django.shortcuts import render
from transport.models import File
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        files = File.objects.filter(owner=request.user).all()
    else:
        files = None
    return render(request, 'home.html', {
        'files': files,
    })
