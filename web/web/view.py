from django.shortcuts import render

def hello(request):
    context = {}
    context['title'] = 'Hello World'
    return render(request,'hello.html',context)