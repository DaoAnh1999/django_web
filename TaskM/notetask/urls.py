from django.urls import path, include
from .views import (Login, TaskListView)

urlpatterns = [
    path('',Login.home, name='home'),
    path('login/',Login.login, name='login'),
    path('logout/',Login.logout, name='logout'),
    path('signup/',Login.signup, name='signup'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskListView.create_task, name='task-create'),
    path('tasks/search/', TaskListView.search_tasks, name='task-search'),
    path('tasks/<int:pk>/update/', TaskListView.update_task, name='task-update'),
    path('tasks/<int:pk>/delete/', TaskListView.delete_task, name='task-delete'),
    path('api/', include('notetask.api.urls')),
]
