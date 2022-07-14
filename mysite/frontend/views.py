from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class New2TemplateView(TemplateView):
    template_name = 'implicitflow_new_2_gapi_async_await.html'


def new3(request):
    return render(request, 'implicitflow_new_3_gapi_callback.html')


class New4View(View):
    template_name = 'authcodeflow_new_1_gis_popup_ux.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       return super(New4View, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print('Google Authcode: ', request.POST.get('code'))
        return JsonResponse({'result': 'success'}, status='200')