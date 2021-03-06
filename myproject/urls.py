"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path, re_path
from django.contrib import admin
from boards import views

urlpatterns = [
    # re_path('^$', views.home, name='home'),  # for regular expression.
    re_path('^$', views.BoardListView.as_view(), name='home'),  # for regular expression.
    # re_path('^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # re_path('^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path('^accounts/', include('accounts.urls')),
    re_path('^boards/', include('boards.urls')),
    re_path('^polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]