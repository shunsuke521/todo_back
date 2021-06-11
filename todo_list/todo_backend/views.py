from rest_framework.views import APIView
from .models import Task

class TaskAPIView(APIView):
    permission_classes = []