from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    # path('signup/',views.user_registration,name='signup'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('details/', views.coursedetails,name='coursedetails'),
    path('courses/', views.courses,name='courses'),
    path('events/', views.events,name='events'),
    path('pricing/', views.pricing,name='pricing'),
    path('trainers/',views.trainers,name='trainers'),
    path('sign-up/', views.user_registration, name='register'),
    path('sign-in/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('contact_us/', views.contact_us, name='contact-us'),

]