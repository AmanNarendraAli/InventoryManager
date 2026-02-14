from django.urls import path
from . import views
app_name = 'authApp' #this is the name of the app, so that we can use it in the urls to refer to the views in this app, for example we can use {% url 'authApp:login' %} to refer to the login view in this app, and it will automatically resolve to the correct url pattern for that view, even if we change the url pattern later, as long as we keep the name of the view the same. This is a good practice to avoid hardcoding urls in the templates and views, and it also makes it easier to change the urls later if needed without having to update all the references to those urls in the code.

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.Home_view, name='home'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]