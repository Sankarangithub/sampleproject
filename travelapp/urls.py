from django.urls import path
from.import views

urlpatterns = [
    path('addDestination/',views.addDestination,name="addDestination"),
    path('getdata/',views.getdata,name="getdata"),
    path('viewdestination/',views.viewdestination,name="viewdestination"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('registerdata/',views.registerdata,name="registerdata"),
    path('logindata/',views.logindata,name="logindata"),
    path('index/',views.index,name="index"),
    
]
