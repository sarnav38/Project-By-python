
from django.urls import path,include
# from .views import snippet_list,snippet_detail
from .views import ArticleAPIView,ArticleAPIViewDetail,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='user')

urlpatterns = [
    path('viewset/',include(router.urls)),
    # path('article/',snippet_list),
    path('article/',ArticleAPIView.as_view()),
    path('generic/article/<int:id>',GenericAPIView.as_view()),
    path('article/<int:pk>/',ArticleAPIViewDetail.as_view())
    # path('article/<int:pk>/',snippet_detail),
]