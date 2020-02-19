"""project_2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import word.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', word.views.home, name="home"),
    path('word/<int:word_id>', word.views.detail, name="detail"),
    path('word/new/', word.views.new, name="new"),
    path('word/create/', word.views.create, name="create"),
    path('word/delete/<int:word_id>', word.views.delete, name="delete"),
    path('word/edit/<int:word_id>', word.views.edit, name="edit"),
    path('word/update/<int:word_id>', word.views.update, name="update"),
]
