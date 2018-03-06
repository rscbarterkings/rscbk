"""rscbk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import *
from django.contrib.auth import views as auth_views

from categories import views as catviews

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^login', auth_views.login, {'template_name': 'home.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name="logout"),

    url(r'myuserdashboard/', myuserdashboard ,name='myuserdashboard'),

    url(r'dashboard/',dashboard),
    url(r'additems/',catviews.additems , name='additems'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)