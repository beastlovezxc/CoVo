'''
@Author: your name
@Date: 2020-04-25 16:52:13
@LastEditTime: 2020-05-04 23:41:18
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Recruit/urls.py
'''
from django.urls import path
from . import views
app_name = 'Recruit'
urlpatterns = [
    # path('to_recruit', views.to_recruit, name='to_recruit')
    path('recruitlist/', views.recruitlist, name='recruitlist'),
    path('agree/<int:apply_id>', views.agree, name='agree'),
    path('refuse/<int:apply_id>', views.refuse, name='refuse'),
]
