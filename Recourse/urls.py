from django.urls import path
from . import views

app_name='Recourse'
urlpatterns = [
    path('', views.Recourse_List),
    path('<int:index>', views.Recourse_Detail),
    path('<str:account>', views.MyRecourse_List),
    path('to_recourse/', views.to_recourse, name='to_recourse'),
    path('record_recourse/', views.record_recourse, name='record_recourse'),
    path('show_list/', views.show_list, name='show_list'),
    # path('helperlist/', views.get_helperlist),
    # path('helperinfo/<int:helper_number>', views.get_helperinfo, name='helperinfo'),
]
