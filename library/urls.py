from django.urls import path
from .views import index, book_list, add_reader, add_book

urlpatterns = [
    path('catalog/', index, name='Main_Page'),
    path('book-list/', book_list, name='books-list'),
    path('add_reader/', add_reader, name='add_reader',),
    path('add_book/', add_book, name='add_book'),
]
