#Created by me not in-build
from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def index2(request):
    return render(request, 'index2.html')
def analyze(request):
    djtext=request.POST.get('text','default')#get the text ##GET REQUEST HAS A LIMIT SO WE USE POST(works for big data)
    #checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get("newlineremover",'off')
    extraspaceremover=request.POST.get("extraspaceremover",'off')
    #charcount=request.POST.get("charcount","off")


    if removepunc == "on":  
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        tejs={'purpose':'Removed Punctuatios','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',tejs)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            tejs={'purpose':'Change to Upper','analyzed_text':analyzed}
            djtext=analyzed
        #return render(request,'analyze.html',tejs)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed=analyzed+char
             tejs={'purpose':'New Line Remover','analyzed_text':analyzed}
             djtext=analyzed
        #return render(request,'analyze.html',tejs)
    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if  not (djtext[index]==" " and djtext[index+1]==" "):
               analyzed=analyzed+char
        tejs={'purpose':'spaceremover','analyzed_text':analyzed}
        djtext=analyzed


    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please Select any operation and Try again!")    


    return render(request,'analyze.html',tejs)