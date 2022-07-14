from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # https://developers.google.com/identity/oauth2/web/guides/migration-to-gis#the_new_way
    path('new1', TemplateView.as_view(template_name='implicitflow_new_1_gis_only.html')),
    path('new2', views.New2TemplateView.as_view()),
    path('new3', views.new3),
    path('new4', views.New4View.as_view()),

    # https://developers.google.com/identity/oauth2/web/guides/migration-to-gis#the_old_way
    path('old1', TemplateView.as_view(template_name='implicitflow_old_1_gapi_client_library.html')),
    path('old2', TemplateView.as_view(template_name='implicitflow_old_2_js_client_library.html')),
]
