from django.urls import path,include
from django.contrib import admin
from django.views.generic import TemplateView
from aplicaciones.usuarios.views import LogOut, userlogin
from aplicaciones.cursos.views import Index_principal
from django.conf import settings

from aplicaciones.carrito.urls import urlpatterns as carrito_urls
from aplicaciones.cursos.urls import urlpatterns as cursos_urls
from aplicaciones.usuarios.urls import urlpatterns as usuarios_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index_principal.as_view(), name='p_index_principal'),
    path('iniciar/', userlogin, name="iniciar_sesion"),
    path('salir/', LogOut, name='cerrar_sesion'),
    path('carrito/', include(
                (
                    carrito_urls,
                    'carrito'
                ), 
                    namespace='app_carrito')
                ),
    path('cursos/', include(
        (
            cursos_urls,
            'cursos'
        ), namespace='app_cursos')),
    path('usuarios/', include(
        (
            usuarios_urls,
            'usuarios'
        ), namespace='app_usuarios')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.views import serve as static_serve
    staticpatterns = static(settings.STATIC_URL, view=static_serve)
    mediapatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = staticpatterns + mediapatterns + urlpatterns
