from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
	
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)