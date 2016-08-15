from django.shortcuts import render
from cms.models import ArticlesModel
from django.http import HttpResponse
# Create your views here.

def show_list(request):
    data = ArticlesModel.objects.all().values()
    return render(request,'article/list.html',{'articles':data})
