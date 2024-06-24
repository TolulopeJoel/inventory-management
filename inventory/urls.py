from rest_framework.routers import DefaultRouter

from inventory.views import InventoryItemViewSet, SupplierViewSet

router = DefaultRouter()
router.register("suppliers", SupplierViewSet)
router.register("inventory-items", InventoryItemViewSet)

urlpatterns = router.urls
