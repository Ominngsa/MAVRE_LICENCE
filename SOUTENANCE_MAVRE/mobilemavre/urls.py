from django.urls import include, path
from rest_framework import routers
from .views import UtilisateurViewSet,login_view

router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',login_view,name='login'),
]