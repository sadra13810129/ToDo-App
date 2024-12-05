from django.urls import path
from .import views

app_name = 'todo'
urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'task-list'),
    path('create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('done/<int:pk>/', views.TaskDoneOrUnDone.as_view(), name = 'task-done-or-undone'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'task-delete')
]
