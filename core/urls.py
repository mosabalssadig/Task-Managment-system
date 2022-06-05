from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index",),
    path("addUser", views.addUser, name="addUser",),
    path("attendance", views.attendance, name="attendance",),
    path("addTask", views.addTask, name="addTask",),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('deleteuser', views.deleteuser, name='deleteuser'),
    path('administration', views.administration, name='administration'),
    path("user/<int:user_id>", views.userview, name="userview"),
    path("task/<int:task_id>", views.taskview, name="taskview"),
    path('deletetask', views.deletetask, name='deletetask'),
    path("reports", views.reports, name="reports",),
    path("history", views.history, name="history",),
    path("update", views.update, name="update",),

]
