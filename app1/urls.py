from unicodedata import name
from django.urls import path 
from .import views

urlpatterns=[
    path('',views.index,name='home'),
    path('<int:id>/',views.qution,name="qution"),
    path('<int:id1>/<int:id2>',views.result,name="result"),

]