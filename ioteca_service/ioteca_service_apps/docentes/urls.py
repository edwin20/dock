from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from .views import CategoriaDocenteViewSet, RegimenDocenteViewSet


# from .api_views import load_menu

#router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'docentes', CategoriaDocenteViewSet)

router.register(r'regimenes', RegimenDocenteViewSet)

RegimenDocenteRouterList = RegimenDocenteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

RegimenDocenteRouterDetail = RegimenDocenteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [

    url(r'^docente/$', CategoriaDocenteViewSet),

    url(r'^regimen/$', RegimenDocenteRouterList),

    url(r'^regimen/(?P<pk>[0-9]+)/$', RegimenDocenteRouterDetail),

    url(r'^', include(router.urls)),
]
