from django.urls import path, include
from . import views
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('passchange/', views.pass_change, name='passchange'),
    path('update/', views.changeData, name='update'),
]
