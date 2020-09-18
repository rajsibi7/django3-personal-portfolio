from django.shortcuts import render
from  .models import Project

def template_portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
    # return HttpResponse('<h1>portfolio works</h1>')

