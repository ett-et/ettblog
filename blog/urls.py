from django.contrib import admin
from django.urls import path, include
from articles import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.articles, name="articles"),
    path('articles/', include("articles.urls")),
]
