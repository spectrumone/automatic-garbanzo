from django.shortcuts import render
from django.views.generic import TemplateView

from project.models import Project


class HomeTemplateView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class CareersTemplateView(TemplateView):
    template_name = 'pages/careers.html'
