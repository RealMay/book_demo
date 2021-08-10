from django.urls import path,include
from rest_framework.routers import DefaultRouter
from books import views

router = DefaultRouter()
router.register('books',views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]