from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ejemplo: /polls/
    path('', views.index, name='index'),
    # ejemplo: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ejemplo: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ejemplo: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
