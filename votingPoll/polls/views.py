from django.shortcuts import render

from django.http import HttpResponse

def index(request):
  return HttpResponse("Sup dawg, this the index.")

def detail(request, question_id):
  response = "You're looking at question %s"

  return HttpResponse(response %question_id)

def results(request, question_id):
  return HttpResponse("This is the result for question %s" %question_id)

def vote(request, question_id):
  return HttpResponse("You're about to vote on question %s" %question_id)