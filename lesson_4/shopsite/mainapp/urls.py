from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='goods_list'),
    path('goods/', mainapp.main, name='goods_list'),
    path('goods/create', mainapp.create_good, name='goods_create'),
]