from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('add/',views.student_create,name='student_create'),
    path('<int:pk>/edit/',views.student_edit,name='student_edit'),
    path('<int:pk>/delete/',views.student_delete,name='student_delete'),
    path('register/',views.register,name='register'),
]
