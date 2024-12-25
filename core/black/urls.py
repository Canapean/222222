from django.urls import path

from .views import ReadCatView, CreateCatView, DetailCatView, UpdateCatView, DeleteCatView

app_name = 'black'

urlpatterns = [
    path('read', ReadCatView.as_view(), name='read'),
    path('detail/<int:pk>', DetailCatView.as_view(), name='detail'),
    path('create', CreateCatView.as_view(), name='create'),
    path('update/<int:pk>', UpdateCatView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteCatView.as_view(), name='delete'),
]