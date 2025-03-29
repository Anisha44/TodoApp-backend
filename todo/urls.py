from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



router = DefaultRouter()
router.register('todos', TodoViewSet)


urlpatterns += router.urls

