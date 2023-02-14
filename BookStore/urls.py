"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from index import views
from index.views import IndexC

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/<int:id>', views.test_html, name='hello'),
    path('test2/', views.test2),
    path('test<int:id>', views.test_html, name='hello4'),
    path('index/', include('index.urls', namespace='first')),
    path('index/test10', IndexC.as_view()),
    # path('index/<str:img>', views.image_html),
    path('user/', include('user.urls', namespace='second')),
    path('welcome/', views.welcome),
]
