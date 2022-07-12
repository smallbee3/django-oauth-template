from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    # https://developers.google.com/identity/oauth2/web/guides/migration-to-gis#the_new_way
    path('new1', TemplateView.as_view(template_name='implicitflow_new_1_gis_only.html')),
]
