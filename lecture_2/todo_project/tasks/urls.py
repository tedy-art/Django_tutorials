from django.views.generic import TemplateView
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, ),
    path('about', TemplateView.as_view(template_name="about.html")),
    path('blog', TemplateView.as_view(template_name="blog.html")),
]