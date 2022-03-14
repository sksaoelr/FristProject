from django.urls import path
from . import views

# http://logalhost/board/
app_name = 'board'
urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('detail/<int:pk>', views.board_detail, name='board_detail'),
    path('detail/<int:pk>/delete/', views.board_delete, name='board_delete')
]