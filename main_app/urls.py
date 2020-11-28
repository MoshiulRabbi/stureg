from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('show_info/',views.show_info,name="show_info"),
    path('show_info/student_info/',views.student_info,name="student_info"),
    path('search_info/',views.search_info,name="search_info"),
    path('search_info/single_info/',views.search_by_id,name="search_by_id"),
    path('show_all_students/',views.show_all_student,name="show_all_students"),
    path('del_registration/',views.del_registration,name="del_registration"),
    path('del_registration/del_id/',views.del_reg_main,name="del_reg_main"),
    path('about_us/',views.about_us,name="about_us"),

]
