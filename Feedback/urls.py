from django.urls import path
from . import views
from django.conf.urls import url
app_name='Feedback'
urlpatterns = [
    path('',views.Feedback_List),
    path('<str:account>',views.Feedback_Detail),
    path('<str:account>/<int:feedback>',views.Feedback_Join),
    # path('apply/<int:activity_number>', views.apply, name='apply'),
]