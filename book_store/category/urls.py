from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_index, name='category_index'),
    path('create/', views.category_create, name='category_create'),
    path('<int:id>/', views.category_show, name='category_show'),
    path('<int:id>/delete', views.category_delete, name='category_delete'),
    path('<int:id>/update/', views.category_update, name='category_update'),
    # path('forms/create', views.book_create_from_forms, name='book_create_from_forms'),
    # path('forms/create_model', views.book_create_from_model_forms, name='book_create_from_model_forms'),
    # path('forms/<int:book_id>/update', views.book_update_model_forms, name='book_update_model_forms')
]
