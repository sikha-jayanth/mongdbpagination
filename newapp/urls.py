
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from newapp import views

urlpatterns = [
    
  path('booklist',views.BooksList.as_view(),name='book'),
  path('paginate',views.BookPaginateCursor.as_view(),name='paginate'),
  path('paginateId',views.BookPaginateId.as_view(),name='paginateId')
    
]
