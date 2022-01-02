from django.urls import path

from . import views
from .views import index, book_list, AddReaderView, AddBookView

urlpatterns = (
    path('', index, name='Main_Page'),
    path('book-list/', book_list, name='books-list'),
    path('add_reader/', AddReaderView.as_view(), name='add_reader'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('give_book/', views.GiveBookView.as_view(), name='give_book'),
    path('take_book/', views.TakeBookBackView.as_view(), name='take_book'),
    path('reset_expiry/<int:pk>/', views.ResetExpiryView.as_view(), name='reset_expiry'),
)
