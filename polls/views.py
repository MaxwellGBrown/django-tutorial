"""Views for the polls app."""
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    """Return index page."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Return details associated with a poll."""
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """Return results of a poll question."""
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    """Return a page which you can vote on a question."""
    return HttpResponse(f"You're voting on question {question_id}")
