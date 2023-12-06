from rest_framework.permissions import *
from rest_framework.generics import *

from .serializers import SignUpSerializer
from .models import User


class CreateUserView(CreateAPIView):
    permission_classes = AllowAny,

    queryset = User.objects.all()
    serializer_class = SignUpSerializer
