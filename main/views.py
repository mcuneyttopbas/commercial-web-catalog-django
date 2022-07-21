from django.shortcuts import redirect, render
from .context import context


def index(request):

    if request.GET:      
        query = request.GET.get("search")
        return redirect(f"/catalog/?search={query}")

    return render(request,"main/index.html",context)

def about(request):
    return render(request,"main/about.html",context)
