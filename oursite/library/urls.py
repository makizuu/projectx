from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/searchResult/', views.searchresults, name='searchresults'),
    #path('home/<slug:acc_name>/searchResult/book_id=<int:book_id>/', views.bookdetail, name='bookdetails'),
    #path('home/<slug:acc_name>/searchResult/book_id=<int:book_id>/bookins_id=<int:bis_id>/', views.borrowoperate, name='borrow'),
]
