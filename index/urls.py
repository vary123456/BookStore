app_name = 'index'   #写在开始位置即可

from django.urls import path
from index import views

urlpatterns = [
    path('base/', views.base_html),
    path('ext1/', views.ext1_html),
    path('filter1/', views.filter1_html),
    path('redict/', views.redict_url),
    path('test222/', views.redict2_url, name='redict2'),
    path('reverse/', views.test_to_reverse),
    path('books/<str:bookname>', views.showbook),
    path('login/', views.login),
    path('login/login2', views.login2),
    path('getcookie/', views.get_cookie_view),
    path('setcookie/', views.set_cookie_view),
    path('login3/', views.login3),
    path('login3/logout/', views.logout),
    path('booksearch/', views.book_search),
    path('booksearchresult/', views.book_search_result),
    path('book_table/', views.book_table),
    path('pub_search/', views.pub_search),
    path('userinforeg', views.userinfo_register),
    path('book_page', views.book_page),
    path('upload/', views.upload),
    path('downloadcsv/', views.downloadcsv),
    path('downloadcsv2/', views.downloadcsv2),
]

