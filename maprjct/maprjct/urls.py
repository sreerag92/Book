"""
URL configuration for maprjct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations.views import Home,prime,Asg,demoview,Book,Booklist,Abc
from operations.views import StudView,Studlist,Book_detailView,std1view,Book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hai/", Home.as_view()),
    path("prm/", prime.as_view()),
    path("am/", Asg.as_view()),
    path("frm/",demoview.as_view()),
    path("book/",Book.as_view()),
    path("bklst/",Booklist.as_view(), name="book-ds"),
    path("student/",StudView.as_view()),
    path("student/list/",Studlist.as_view()),
    path("bk/<int:pk>",Book_detailView.as_view(), name="book-dt"),
    path("bk/<int:pk>/remove",Book_delete.as_view(), name="book-dlt"),
    path("std/",std1view.as_view()),
    path("abcd/", Abc.as_view()),


]
