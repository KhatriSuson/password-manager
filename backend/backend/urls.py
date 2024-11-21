from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, UserProfileViewSet
from credentials.views import CredentialViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', UserProfileViewSet)
router.register('credentials', CredentialViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
