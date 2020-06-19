from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import path
from django.views import generic
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

#app_name = 'tejas'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projectlist', views.Project_index, name='project_index'),
    path('<int:pk>', views.Project_detail, name='project_detail'),
    path('resume', views.Resume, name='resume'),
    path('contact', views.Contact, name='contact'),
    path('research', views.ResearchPaperListView.as_view(), name='research'),
    path('researchpaper/<int:pk>', views.ResearchPaperDetailView.as_view(), name='researchpaper'),
    path('postlist', views.PostList.as_view(), name="post_list"),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('success', views.SuccessView, name='success'),
    ]
