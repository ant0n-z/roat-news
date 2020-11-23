# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:20:03 2020

@author: az
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
