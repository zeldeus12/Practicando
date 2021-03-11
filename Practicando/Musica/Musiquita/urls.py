
from django.urls import path
from .views import primera,segunda,login, formulario
urlpatterns = [
path ('Inicio/', primera , name='homes'),
path ('Secundario/', segunda, name='dosh'),
path ('Login/', login, name='login'),
path ('Formulario/', formulario, name='Form'),

]
