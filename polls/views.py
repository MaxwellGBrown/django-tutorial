"""Views for the polls app."""
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
    """View to list the polls."""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return queryset."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """View to see poll details."""
    template_name = "polls/detail.html"
    model = Question


class ResultsView(generic.DetailView):
    """View to see poll results."""
    template_name = "polls/results.html"
    model = Question


def vote(request, question_id):
    """Return a page which you can vote on a question."""
    question = get_object_or_404(Question, pk=question_id) 
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": Question,
            "error": "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
