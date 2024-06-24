from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from accounts.permissions import IsEmployee

from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsEmployee]


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsEmployee()]
