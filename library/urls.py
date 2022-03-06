from django.urls import path

from . import views

app_name = "library"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/searchResult/", views.searchresults, name="searchresults"),
    path("borrow/<int:id>", views.borrow, name="borrow"),
    path("unborrow/<int:id>", views.unborrow, name="unborrow"),
]
