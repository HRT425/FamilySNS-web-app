from django.urls import path, include
from . import views

app_name = 'roomapp'

urlpatterns = [
    path('', views.notfunc, name='not'),
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('main/', views.mainfunc, name='main'),
    path('list/', views.HomeList.as_view(), name='list'),
    path('mylist/', views.MyList.as_view(), name='mylist'),
    path('create_list/', views.ListCreate.as_view(), name="create_list"),
    path('list/detail/<int:pk>/update', views.ListUpdate.as_view(), name="update_list"),
    path('list/detail/<int:pk>', views.ListDetail.as_view(), name='detail_list'),
    path('list/delete/<int:pk>', views.ListDelete.as_view(), name='delete_list'),
    path('schedule/', include('schedule.urls'), name="schedule"),
]