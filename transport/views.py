import imp
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import File
from .forms import UploadForm

# Create your views here.


class UploadView(LoginRequiredMixin, CreateView):
    model = File
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('display:home')
