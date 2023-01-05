from django.urls import path
from dictionary import views

urlpatterns = [
    path('search_word/', views.search_word, name='search_word'),
    path('list_words/', views.list_words, name='list_words'),
    path('word_meaning/<int:word_id>/', views.word_meaning, name='word_meaning'),
]
