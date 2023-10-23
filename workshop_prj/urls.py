"""
URL configuration for workshop_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
import workshop_main.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
		# min 변경사항
		# main / startTest / test 로 url 분리
    path('', workshop_main.views.main, name='main'),
		path('startTest/', workshop_main.views.startTest, name='startTest'),
		path('test/', workshop_main.views.test, name='test'),
    path('guestbook/', workshop_main.views.guestbook, name='guestbook'),
    path('introduce/', workshop_main.views.introduce, name='introduce'),
    path('cast/', workshop_main.views.cast, name='cast')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
