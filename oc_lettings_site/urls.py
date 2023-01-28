from django.contrib import admin
from django.urls import path, include

from . import views
import lettings.views
import profiles.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),

]

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('lettings/', lettings.views.index, name='lettings_index'),
#     path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
#     path('profiles/', profiles.views.index, name='profiles_index'),
#     path('profiles/<str:username>/', profiles.views.profile, name='profile'),
# ]
#


