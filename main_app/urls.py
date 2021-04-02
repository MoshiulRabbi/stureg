from os import name
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    # path('add_reg/',views.add_reg,name="add-reg"),
    # path('all_student/',views.all_student,name="all_student"),
    # path('search',views.search,name="search"),

    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('search/',views.search,name="search"),
    path('about/',views.about,name="about"),
    path('show_all_students/',views.show_all_student,name="show_all_students"),
    path('add_student',views.add_student,name="add_student"),
    path('delete/<int:pk>',views.delete,name="delete"),

]
