# BY NA
import string
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req,'index.html')
def analyze(req):
    matter=req.GET.get('text',None)
    orig=matter
    rem_punc=req.GET.get('rem_punc','OFF')
    caps=req.GET.get('caps','OFF')
    delln=req.GET.get('delln','OFF')
    delsp=req.GET.get('delsp','OFF')
    ccount=req.GET.get('ccount','OFF')
    work=''
    if rem_punc=='on':
        mat=''.join(i for i in matter if i not in string.punctuation)
        work+="REMOVED PUNCTUATIONS\n"
        matter=mat
    if caps=='on':
        mat = ' '.join(ele.capitalize() for ele in matter.replace('\n',' ').split(' '))
        work+="CAPITALIZED\n"
        matter=mat
    if delln=='on':
        mat = matter.replace('\n', 'N')
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
    print(work)
    return render(req,'work.html',dic)