from django.urls import path 
from tasks import views


urlpatterns = [
	path("", views.task_list, name="task_list"),
    path("<int:id>", views.task_view, name="task_view"),
    path("create", views.create_task, name="create_task"),
    path("/update/<int:id>", views.update_task, name="update_task")
]
