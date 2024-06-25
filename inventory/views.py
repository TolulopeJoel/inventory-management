from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import IsEmployeeOrAdmin

from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsEmployeeOrAdmin]


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def get_permissions(self):
        if self.action not in ['list', 'retrieve']:
            return [IsAuthenticated(), IsEmployeeOrAdmin()]
        return [AllowAny()]
