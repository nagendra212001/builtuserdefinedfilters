from django.shortcuts import render

# Create your views here.

def builtinfilter(request):
    import datetime
    dt=datetime.date.today
    d={'name':'mY nAmE IS nAgEnDRa', "dt":dt,"c":0}
    return render(request,"builtinfilter.html",d)

def userdefinedfilters(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefinedfilters.html',d)