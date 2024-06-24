from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from inventory.models import InventoryItem, Supplier
from inventory.serializers import InventoryItemSerializer

from ..models import InventoryItem, Supplier


class InventoryAPITestCase(TestCase):
    """Test case for Inventory API endpoints."""

    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(
            name="Test Supplier", contact_info="test@example.com"
        )
        self.item = InventoryItem.objects.create(
            name="Test Item", description="Test Description", price=10.00
        )
        self.item.suppliers.add(self.supplier)

    def test_get_suppliers(self):
        url = reverse("supplier-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_inventory_items(self):
        url = reverse("inventoryitem-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class InventoryItemSerializerTestCase(APITestCase):
    """Test case for InventoryItemSerializer."""

    def setUp(self):
        self.supplier1 = Supplier.objects.create(name="Supplier 1")
        self.supplier2 = Supplier.objects.create(name="Supplier 2")
        self.item_data = {
            "name": "Test Item",
            "description": "Test Description",
            "quantity": 10,
            "price": 10.00,
            "supplier_ids": [self.supplier1.id, self.supplier2.id],
        }

    def test_create_inventory_item(self):
        serializer = InventoryItemSerializer(data=self.item_data)
        self.assertTrue(serializer.is_valid())
        item = serializer.save()
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 10.00)
        self.assertEqual(item.suppliers.count(), 2)
        self.assertIn(self.supplier1, item.suppliers.all())
        self.assertIn(self.supplier2, item.suppliers.all())

    def test_update_inventory_item(self):
        item = InventoryItem.objects.create(
            name="Original Item", quantity=5, price=5.00
        )
        item.suppliers.add(self.supplier1)

        update_data = {
            "name": "Updated Item",
            "quantity": 15,
            "price": 15.00,
            "supplier_ids": [self.supplier2.id],
        }
        serializer = InventoryItemSerializer(item, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_item = serializer.save()

        self.assertEqual(updated_item.name, "Updated Item")
        self.assertEqual(updated_item.quantity, 15)
        self.assertEqual(updated_item.price, 15.00)
        self.assertEqual(updated_item.suppliers.count(), 1)
        self.assertIn(self.supplier2, updated_item.suppliers.all())

    def test_single_supplier_id(self):
        data = self.item_data.copy()
        data["supplier_ids"] = self.supplier1.id
        serializer = InventoryItemSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        item = serializer.save()
        self.assertEqual(item.suppliers.count(), 1)
        self.assertIn(self.supplier1, item.suppliers.all())

    def test_serialization(self):
        item = InventoryItem.objects.create(name="Test Item", quantity=10, price=10.00)
        item.suppliers.add(self.supplier1, self.supplier2)
        serializer = InventoryItemSerializer(item)
        data = serializer.data
        self.assertEqual(data["name"], "Test Item")
        self.assertEqual(data["quantity"], 10)
        self.assertEqual(len(data["suppliers"]), 2)
        self.assertIn("id", data["suppliers"][0])
        self.assertIn("name", data["suppliers"][0])
