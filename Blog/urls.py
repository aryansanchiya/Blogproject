from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("post/<int:id>",views.post,name='post'),
    path("contact",views.contact,name='contact'),
    path("blog",views.blog,name="blog"),
    path('projects',views.projects,name='projects'),
    re_path(r'^tracking/', include('tracking.urls')),
]