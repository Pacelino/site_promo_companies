from django.shortcuts import render

from .models import Company

# Create your views here.
def company_render(request):
    return render(request, "company.html", {'companys': Company.objects.all()})