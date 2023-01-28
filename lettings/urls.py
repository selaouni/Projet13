from django.contrib import admin
from django.urls import path

import lettings.views

app_name = 'lettings'
urlpatterns = [

    path('lettings/', lettings.views.index, name='index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),

]
