from django.urls import include, path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, TestView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('time/', TestView.as_view()),
]