from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def editor(request):
   return render(request, "editor.html")

def graph(request):
  return render(request, "graph.html")
