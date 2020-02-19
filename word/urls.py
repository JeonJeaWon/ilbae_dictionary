from django.urls import path
import word.views

urlpatterns = [
    path('word/<int:word_id>', word.views.detail, name="detail"),
    path('word/new/', word.views.new, name="new"),
    path('word/create/', word.views.create, name="create"),
    path('word/delete/<int:word_id>', word.views.delete, name="delete"),
    path('word/edit/<int:word_id>', word.views.edit, name="edit"),
    path('word/update/<int:word_id>', word.views.update, name="update"),
]