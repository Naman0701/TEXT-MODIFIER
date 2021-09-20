# BY NA
import string
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req,'index.html')
def analyze(req):
    matter=req.GET.get('text','NAN')
    orig=matter
    rem_punc=req.GET.get('rem_punc','OFF')
    caps=req.GET.get('caps','OFF')
    delln=req.GET.get('delln','OFF')
    delsp=req.GET.get('delsp','OFF')
    ccount=req.GET.get('ccount','OFF')
    work=''
    if rem_punc=='on':
        mat=''
        for i in matter:
            if i  not in string.punctuation:
                mat+=i
        work+="REMOVED PUNCTUATIONS\n"
        matter=mat
    if caps=='on':
        mat=''
        mat = ' '.join(ele.capitalize() for ele in matter.replace('\n',' ').split(' '))
        work+="CAPITALIZED\n"
        matter=mat
    if delln=='on':
        mat=''
        mat = matter.replace('\n', '').strip()
        work+="DELETED NEW LINE\n"
        matter=mat
    if delsp=='on':
        mat=''
        for index,char in enumerate(matter):
            if not(matter[index]==' ' and matter[index+1]==' '):
                mat+=char
        # print(f'{matter}\n {mat}')
        work+="DELETED EXTRA SPACES\n"
        matter = mat
    if ccount=='on':
        mat=''
        mat=matter
        mat += f'\n{len(matter.strip())} AFTER DELETING TERMINATING WHITE SPACES'
        orig += f'\n{len(orig)} BEFORE DELETING TERMINATING WHITE SPACES'
        work+="LENGTH OF TEXT\n"
        matter = mat
    else:
        mat=matter
    dic={
        'work':work,
        'old': orig,
        'new': mat,

    }
    print(work)
    return render(req,'work.html',dic)