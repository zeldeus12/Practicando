
from django.urls import path
from .views import primera,segunda,login, formulario,admin,agregarcanciones,agregarartistas,linkeimagen
urlpatterns = [
path ('Inicio/', primera , name='homes'),
path ('Secundario/', segunda, name='dosh'),
path ('Login/', login, name='login'),
path ('Formulario/', formulario, name='Form'),
path ('Admin/', admin, name='Admin'),
path ('AgregarCanciones/', agregarcanciones, name='Agregacanciones'),
path ('AgregarArtistas/', agregarartistas, name='Agregaartistas'),
path ('LinkeImagen/', linkeimagen, name='Admin'),

]
