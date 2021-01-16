from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for User model."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post', 'get'])
    def active(self, request, *args, **kwargs):
        """API endpoint that allows to view active users."""
        active_users = self.queryset.filter(is_active=True)
        serializer = self.serializer_class(instance=active_users, many=True)
        return Response(serializer.data)
