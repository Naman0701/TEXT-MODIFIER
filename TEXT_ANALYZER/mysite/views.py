# BY NA
import string
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req,'index.html')
def analyze(req):
    matter=req.POST.get('text',None).replace('\r','')
    orig=matter
    rem_punc=req.POST.get('rem_punc','OFF')
    caps=req.POST.get('caps','OFF')
    delln=req.POST.get('delln','OFF')
    delsp=req.POST.get('delsp','OFF')
    ccount=req.POST.get('ccount','OFF')
    work=''
    if rem_punc=='on':
        mat=''.join(i for i in matter if i not in string.punctuation)
        work+="REMOVED PUNCTUATIONS\n"
        matter=mat
    if caps=='on':
        mat=matter.title()
        work+="CAPITALIZED\n"
        matter=mat
    if delln=='on':
        mat = matter.replace('\n', '')
        work+="DELETED NEW LINE\n"
        matter=mat
    if delsp=='on':
        mat=''.join(matter[i] for i in range(len(matter)) if not(matter[i]==' ' and matter[i+1]==' '))
        work+="DELETED EXTRA SPACES\n"
        matter = mat
    if ccount=='on':
        mat=matter
        mat += f'\nCHAR COUNT: {len(matter)}'
        orig += f'\nCHAR COUNT: {len(orig)}'
        work+="CHAR COUNT\n"
        matter = mat
    dic={
        'work':work,
        'old': orig,
        'new': matter,

    }
    return render(req,'work.html',dic)