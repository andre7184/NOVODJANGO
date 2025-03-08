from rest_framework import viewsets

from api.models import CustonUser
from api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustonUser.objects.all()
    serializer_class = UserSerializer