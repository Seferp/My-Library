from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>/delete/', views.DeleteBook.as_view(), name='delete_book'),
    path('<int:book_id>/update/', views.UpdateBook.as_view(), name='update_book'),
]
