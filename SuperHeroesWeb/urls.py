from django.urls import path
from .views import index, listaPersonajes,form_personaje,form_mod_personaje,form_del_personaje

urlpatterns=[
    path('',index,name="index"),
    path('listaPersonajes',listaPersonajes,name="listaPersonajes"),
    path('form_personaje',form_personaje,name="form_personaje"),
    path('form_mod_personaje/<id>',form_mod_personaje,name="form_mod_personaje"),
    path('form_del_personaje/<id>',form_del_personaje,name="form_del_personaje"),
]