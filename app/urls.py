from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('page404/', Error.as_view(), name='page404'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('courses/', Courses.as_view(), name='courses'),
    path('team/', Team.as_view(), name='team'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
]
