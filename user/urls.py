app_name = 'user'   #写在开始位置即可

from django.urls import path
from user import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('regsta/', views.register_start),
    path('regres/', views.register_result),
    path('login/', views.login),
    # path('login/', LoginView.as_view(template_name='user/login.html'))
]

