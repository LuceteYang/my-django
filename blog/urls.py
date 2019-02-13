from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'blog'
urlpatterns = [
    # 순서에 따라 먼저 탐
    path('', views.ListView.as_view(), name='list'),
    path('json-response/', views.get_json_response),
    url(r'^write/$', login_required(views.WriteView.as_view()), name='write'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='view'),	# pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다. \d은 문자를 제외한 숫자
    url(r'^hello/$', views.hello),
    url(r'^view/(?P<pk>\d+)/remove/$', views.article_remove, name='article_remove'),
    
    url(r'^join/$', views.signup, name='join'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    # url(r'json/', views.jsonctrl),
]
