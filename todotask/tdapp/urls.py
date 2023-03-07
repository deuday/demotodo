from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:Taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listview/', views.tdlist.as_view(), name='listview'),
    path('detailview/<int:pk>/', views.tddetail.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.tdupdate.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.tddelete.as_view(), name='deleteview')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
