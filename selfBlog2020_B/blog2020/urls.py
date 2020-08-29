from django.urls import path, re_path
from . import views

urlpatterns = [
    path('LeaveMessages/', views.LeaveMessagesView.as_view()),
    path('ReplyMessages/', views.ReplyMessagesView.as_view()),
    path('Blogs/', views.BlogView.as_view({'get': 'list'})),
    re_path('^Blogs/(?P<pk>\d+)/$', views.BlogView.as_view({'get': 'retrieve'})),
    path('Musics/', views.MusicView.as_view()),
    path('Cartoons/', views.CartoonView.as_view({'get': 'list'})),
    re_path('^Cartoons/(?P<pk>\d+)/$', views.CartoonView.as_view({'get': 'retrieve'})),
    re_path('^WebReadPerson/(?P<pk>\d+)/$', views.WebReadPersonView.as_view()),
]
