from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from .views import ExperienciaAcademicaViewSet


# from .api_views import load_menu

#router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'xacademico',  ExperienciaAcademicaViewSet)

ExperienciaAcademicaRouterList = ExperienciaAcademicaViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

ExperienciaAcademicaRouterDetail = ExperienciaAcademicaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [

    url(r'^xacademico/$', ExperienciaAcademicaRouterList),

    url(r'^xacademico/(?P<pk>[0-9]+)/$', ExperienciaAcademicaRouterDetail),

    url(r'^', include(router.urls)),
]
