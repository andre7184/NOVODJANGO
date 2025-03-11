from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.api_views import Login, UserViewSet

# from .views.api_views import AlunoViewSet
from .views.web_views import home
from .views.web_views import CriarAluno
from .views.web_views import login

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', Login.as_view(), name='loginAPI'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('criarAluno/', CriarAluno, name='criarAluno'),
]