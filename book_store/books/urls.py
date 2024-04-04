from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('', views.home, name='home_page'),
    # path('<int:book_id>/', views.book_details, name='book_page'),
    path('contact/', views.contact, name='contact_page'),
    path('about/', views.about, name='about_page'),
    path('', views.books_index, name='index_page'),
    path('<int:book_id>/', views.book_show, name='book_show'),
    path('<int:book_id>/delete', views.book_delete, name='book_delete'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:book_id>', views.book_update, name='book_update'),
]
