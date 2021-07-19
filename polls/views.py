"""Views for the polls app."""
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    """Return details associated with a poll."""
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    """Return results of a poll question."""
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    """Return a page which you can vote on a question."""
    return HttpResponse(f"You're voting on question {question_id}")
