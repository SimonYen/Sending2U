from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse, Http404, FileResponse
from django.shortcuts import redirect
import os
from .models import File
from .forms import UploadForm

# Create your views here.


class UploadView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = File
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('display:home')
    success_message = 'Uploaded successfully.🍉 '

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def download(request, pk: int):
    file = File.objects.filter(pk=pk).first()
    if file is None:
        raise Http404
    if file.owner != request.user:
        return HttpResponse('This file doesn\'t belong to you!')
    try:
        response = FileResponse(open(file.raw_data.path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response[
            'Content-Disposition'] = 'attachment; filename=' + file.raw_data.name
    except:
        raise Http404
    return response


def delete(request, pk: int):
    file = File.objects.filter(pk=pk).first()
    if file is None:
        return reverse('display:home')
    if file.owner != request.user:
        return reverse('display:home')
    if os.path.isfile(file.raw_data.path):
        os.remove(file.raw_data.path)
    file.delete()
    return redirect(reverse('display:home'))
