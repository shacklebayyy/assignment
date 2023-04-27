
from django.urls import path
from . import views

urlpatterns = [
    path('',views.crudd, name='cruds' ),
    path('insert',views.insertData,name ="InsertData"),
     path('update/<id>',views.UpdateData,name ="updateData")
]