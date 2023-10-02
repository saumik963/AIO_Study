from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.tooks, name='tools'),
    path('Notes/', views.Note, name='Note'),
    path('Videos/', views.Videos, name='Videos'),
    path('is_complete/<int:id>/', views.NoteComplete, name='complete'),
    path('edit/<int:pk>/', views.NoteUpdate, name='edit'),
    path('delete/<int:id>/', views.DeleteNote, name='delete'),
    path('Read_books/', views.books, name='books'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('wiki/', views.wiki, name='wiki'),

]
