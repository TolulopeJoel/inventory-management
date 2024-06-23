from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from inventory.models import Supplier, InventoryItem
from inventory.serializers import SupplierSerializer


class SupplierAPITestCase(TestCase):
    """Test case for Supplier API endpoints."""

    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_info="test@example.com"
        )
        self.item = InventoryItem.objects.create(
            name="Test Item",
            description="Test Description",
            price=10.00
        )
        self.item.suppliers.add(self.supplier)

    def test_get_suppliers(self):
        url = reverse('supplier-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_supplier_detail(self):
        url = reverse('supplier-detail', kwargs={'pk': self.supplier.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Test Supplier")


class SupplierSerializerTestCase(APITestCase):
    """Test case for SupplierSerializer."""

    def setUp(self):
        self.item1 = InventoryItem.objects.create(name="Item 1", price=10.00)
        self.item2 = InventoryItem.objects.create(name="Item 2", price=20.00)
        self.supplier_data = {
            "name": "Test Supplier",
            "contact_info": "test@example.com",
        }

    def test_create_supplier(self):
        serializer = SupplierSerializer(data=self.supplier_data)
        self.assertTrue(serializer.is_valid())
        supplier = serializer.save()
        # self.item1.suppliers.add(supplier)
        # self.item2.suppliers.add(supplier)
        supplier.items.add(self.item1, self.item2)

        self.assertEqual(supplier.name, "Test Supplier")
        self.assertEqual(supplier.contact_info, "test@example.com")
        self.assertEqual(supplier.items.count(), 2)
        self.assertIn(self.item1, supplier.items.all())
        self.assertIn(self.item2, supplier.items.all())

    def test_update_supplier(self):
        supplier = Supplier.objects.create(
            name="Original Supplier", contact_info="original@example.com")
        supplier.items.add(self.item1)

        update_data = {
            "name": "Updated Supplier",
            "contact_info": "updated@example.com",
        }
        serializer = SupplierSerializer(
            supplier, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_supplier = serializer.save()

        self.assertEqual(updated_supplier.name, "Updated Supplier")
        self.assertEqual(updated_supplier.contact_info, "updated@example.com")
        self.assertEqual(updated_supplier.items.count(), 1)
    #     self.assertIn(self.item2, updated_supplier.items.all())

    def test_serialization(self):
        supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_info="test@example.com"
        )
        supplier.items.add(self.item1, self.item2)
        serializer = SupplierSerializer(supplier)
        data = serializer.data
        self.assertEqual(data['name'], "Test Supplier")
        self.assertEqual(data['contact_info'], "test@example.com")
        self.assertEqual(len(data['items']), 2)
        self.assertIn('id', data['items'][0])
        self.assertIn('name', data['items'][0])
