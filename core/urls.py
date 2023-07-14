"""
URL configuration for core project.

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
from movie import views as moviesViews
from django.conf.urls.static import static
from django.conf import settings

#as 어라이싱
#돌아가기 하기위해 home path에  name='home'를 추가
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',moviesViews.home, name='home'),
    path('about/',moviesViews.about),
    path('signup/',moviesViews.signup, name='signup'),

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

