from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

# this setup allows us to perform CRUD operations on our 'TODO' model via the rest_framework model
router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
