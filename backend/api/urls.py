from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.api_views import AlunoViewSet
from .views.web_views import home

router = DefaultRouter()
router.register('alunos', AlunoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name='home')
]