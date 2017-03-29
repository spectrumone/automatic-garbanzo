from django.views.generic import DetailView
from .models import Project

# Create your views here.


class ProjectDetailView(DetailView):
    template_name = 'pages/project.html'
    model = Project
