from django.shortcuts import render

from django.db.models import F
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).get(pk=question_id)
        context = {
            'question': question,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    context = {}

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context['question'] = question
        context['error_message'] = "You didn't select a choice"

        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes = F('votes') + 1  # F elimina la condicion de carrera
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

