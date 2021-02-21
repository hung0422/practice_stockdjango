from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('predict/', views.predict, name='predict'),
    path('detail/<str:date>/', views.detail, name='detail'),
    path('bookkeeping/', views.bookkeeping, name='bookkeeping'),
    path('categorysetting/', views.categorysetting, name='categorysetting'),
    path('categorydelete/<str:id>/', views.categorydelete, name='categorydelete'),
    path('bookdelete/<str:id>/', views.bookdelete, name='bookdelete')
]
