from django.shortcuts import render
from .models import Men, Portfolio, Blog

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView


def index(request):
    m1 = Portfolio.objects.all()
    m2 = Men.objects.all()

    contex = {
        "Portfolio": m1,
        'Local': m2,
       
    }
    return render(request, ["index.html", "portfolio.html"], contex)


class PortfolioViews(ListView):
    model = Portfolio
    template_name = "portfolio.html"
    context_object_name = "Portfolio"
    
    
class BlogViews(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "Blog"