from django.shortcuts import render

# Create your views here.


def Home_view(request):
    return render(request,'home.html')

def Aboutus_view(Request):
    return render(Request,'about.html')

def Service_view(Request):
    return render(Request,'service.html')

def Gallery_view(Request):
    return render(Request,'gallery.html')

def Contact_view(Request):
    return render(Request,'gallery.html')