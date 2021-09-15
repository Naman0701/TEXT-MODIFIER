# BY NA
import string

from django.http import HttpResponse
from django.shortcuts import render
# import os
#
# print(os.listdir())
# # print(fil)
# def index(req):
#     return HttpResponse('''<a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" target="_"> CWH </a>''')
#
#
# def about(req):
#     fil = open('one.txt', 'r+')
#     return HttpResponse(fil.read())
def index(req):
    return render(req,'homepg.html')
def removepunc(req):
    matter=req.GET.get('text','NAN')
    mat=matter
    # print(matter)
    for i in matter:
        if i in string.punctuation:
            matter=matter.replace(i,'')
    dic={
        'name': 'REMOVE PUNC',
        'old_op': 'TEXT BEFORE REMOVING PUNC:',
        'new_op': 'TEXT AFTER REMOVING PUNC:',
        'old':mat,
        'new': matter
    }
    return render(req, 'work.html',dic)

def cap1(req):
    matter=req.GET.get('text','NAN')
    mat=' '.join(ele.capitalize() for ele in matter.split(' '))
    dic={
        'name': 'CAPITALIZE FIRST',
        'old_op': 'TEXT BEFORE CAPITALIZING:',
        'new_op': 'TEXT AFTER CAPITALIZING:',
        'old':matter,
        'new':mat
    }
    return render(req,'work.html',dic)
def newlndel(req):
    matter = req.GET.get('text', 'NAN')
    mat=matter.replace('\n','').strip()
    print(len(matter))
    print(len(mat))
    dic = {
        'name': 'DELETE NEW LINE',
        'old_op': 'TEXT BEFORE DELETING NEW LINE:',
        'new_op': 'TEXT AFTER DELETING NEW LINE:',
        'old': matter,
        'new': mat
    }
    return render(req, 'work.html', dic)
def spacedel(req):
    matter = req.GET.get('text', 'NAN')
    mat=matter.replace(' ','')
    dic = {
        'name': 'DELETE SPACES',
        'old_op': 'TEXT BEFORE REMOVING SPACES:',
        'new_op': 'TEXT AFTER REMOVING SPACES:',
        'old': matter,
        'new': mat
    }
    return render(req, 'work.html', dic)
def charcount(req):
    matter = req.GET.get('text', 'NAN')
    mat=matter.strip()
    dic = {
        'name': 'CHAR COUNT',
        'old_op': 'TEXT BEFORE STRIPPING SPACES AND NEW LINES AT ENDS:',
        'new_op': 'TEXT AFTER STRIPPING SPACES AND NEW LINES AT ENDS:',
        'old': len(matter),
        'new': len(mat)
    }
    return render(req, 'work.html', dic)