from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):
    t_proj = Project.objects.all()
    return render(request, template_name='portfolio.html', context={'tl_proj': t_proj})

def home(request):
    return render( request,template_name='index.html')
