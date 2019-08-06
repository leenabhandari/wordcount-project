from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    ourtext = request.GET['fulltext']
    wordlist = ourtext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

        sortedlist = sorted(worddict.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'countnum':len(wordlist),'ourtext':ourtext,'worddict': sortedlist})

def about(request):
    return render(request,'about.html')
