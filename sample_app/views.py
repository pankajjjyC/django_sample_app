from django.shortcuts import render

# Create your views here.
def mainview(r):
    return render(r,'index.html',{})


def index2(r):
    str=" hello how are you"
    return render(r,'index2.html',{'int':str})

def index3(r):
    str=" index 3 page welcomes you"
    return render(r,'index3.html',{'int':str})
