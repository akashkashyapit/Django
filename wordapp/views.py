from django.shortcuts import render
from django.http import HttpResponse
import operator

def homepage(request):
    return render(request, 'home.html', {'aka':"Akash Kashyap"})


def count(request):
    data = request.GET['textarea']
    wlist = data.split()
    length = len(wlist)
    wdict = {}
    for w in wlist:
        if w in wdict:
            wdict[w]+=1
        else:
            wdict[w]=1

    listw = sorted(wdict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'aka':listw, 'length':length})


def contact(request):
    return render(request, 'contact.html', {'aka':"Akash Kashyap contact"})
