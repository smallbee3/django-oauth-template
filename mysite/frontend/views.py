from django.shortcuts import render
from django.views.generic import TemplateView


class New2TemplateView(TemplateView):
    template_name = 'implicitflow_new_2_gapi_async_await.html'


def new3(request):
    return render(request, 'implicitflow_new_3_gapi_callback.html')
