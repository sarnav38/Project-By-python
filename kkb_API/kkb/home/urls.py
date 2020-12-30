from django.urls import path,include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('kkb', ArticleViewSet, basename='user')

urlpatterns = [
    path('kkb/', include(router.urls)),
]