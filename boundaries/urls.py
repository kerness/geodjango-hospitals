from rest_framework.routers import DefaultRouter
from .views import BoundaryViewSet

router = DefaultRouter()
router.register(prefix='api/v1/boundaries', viewset=BoundaryViewSet, basename='Boundary')

urlpatterns = router.urls
