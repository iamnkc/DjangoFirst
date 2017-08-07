# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions,choice
from django.shortcuts import render,get_object_or_404
from django.http import Http404


def index(request):
    question = Questions.objects.all()
    context = {'ques' : question}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    question = get_object_or_404(Questions,pk=question_id,)
    return render(request,'polls/details.html',{'ques':question})

def results(request,question_id):
    return HttpResponse('<h1> Hello World</h1>');
def vote(request,question_id):
    return HttpResponse('<h1> Hello World</h1>')