from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('Test/', views.TestListAPIView.as_view()),
    path('Login/', views.LoginAPIView.as_view()),
    path('Register/', views.RegisterAPIView.as_view()),
    path('Questions/', views.QuestionsView.as_view({'get': 'list', 'post': 'create', 'patch': 'update'})),
    url('^Questions/(?P<pk>\d+)/$',
        views.QuestionsView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('Questionnaires/', views.QuestionnaireListAPIView.as_view({'get': 'list', 'post': 'create', })),
    path('allQuestionnaires/', views.allQuestionnaireListAPIView.as_view()),
    url('^Questionnaires/(?P<pk>\d+)/$',
        views.QuestionnaireListAPIView.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    path('ClassList/', views.ClassListListAPIView.as_view()),
    path('Answers/', views.AnswerAPIView.as_view()),
    path('Options/', views.OptionAPIView.as_view({'post': 'create'})),
    url('Options/(?P<pk>\d+)/$', views.OptionAPIView.as_view({'get': 'getAnswerList', 'delete': 'destroy'})),
    path('Score/questionaire/', views.ScoreView.as_view()),
    path('Check/', views.Check.as_view({'get': 'OK'})),
    path('Question/', views.UserQuestionListAPIview.as_view()),
]
