from django.urls import path

from app import views
from app.views import *

urlpatterns=[
    path('',index,name="home"),
    # path('add_news/',add_news,name="add_news"),
    # path('detail_new/<int:pk>/',detail_new,name="detail_new"),
    path("category/<int:pk>/",category,name="category"),

]