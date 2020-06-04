from django.urls import path

from booking import views


app_name = 'booking'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search'),
    path('booking/', views.book_ticket, name='book_ticket'),
    path('ticket/', views.get_ticket, name='get_ticket'),
    
]
