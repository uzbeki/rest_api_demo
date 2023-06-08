# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from api_app.serializers import TodoSerializer
from api_app.models import TodoModel



class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]

