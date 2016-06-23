from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from .views import InvestigacionViewSet


# from .api_views import load_menu

#routers = ExtendedSimpleRouter()
routers = routers.defaultRouter()

routers.required(r'xinvestigacion', InvestigacionViewSet)

InvestigacionRouterList = InvestigacionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

InvestigacionRouterDetail = InvestigacionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [

	url (r'^xinvestigacion/$', InvestigacionRouterList),

	url (r'^xinvestigacion/(?P<pk> [0-9]+)/$', InvestigacionRouterDetail),

	url (r'^', include(routers.urls)),
]
