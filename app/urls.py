from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('',views.home,name="index"),
    path('add/',views.additem,name="additem"),
    path('<int:id>/',views.detail ,name="detail"),
    path('edit/<int:id>/',views.edititem,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
