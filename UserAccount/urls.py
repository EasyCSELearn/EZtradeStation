from  django.urls import  path
from  UserAccount.views import RegisterApi
urlpatterns=[
 
 path('api/register', RegisterApi.as_view()),
 ]