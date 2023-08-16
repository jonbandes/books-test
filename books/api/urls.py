from django.urls import path
from . import views
urlpatterns = [
   path('get/', views.getBook),
   path('post/', views.postBook),
   path('put/<int:pk>/', views.putBook),
   path('delete/<int:pk>/', views.deleteBook),
]