from rest_framework.viewsets import ModelViewSet
from users.api.serializers import UserSerializer
from users.models import User 
from django.contrib.auth.hashers import make_password
# Create your views here.

class UserApiWieset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.object.all()
    def create(self, request, *args, **kwargs):
        request.data('password') = make_password
        return super().create(request, *args,**kwargs)