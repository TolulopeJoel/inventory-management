from rest_framework import serializers

from .models import InventoryItem, Supplier


class PublicInventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name']


class SupplierSerializer(serializers.ModelSerializer):
    items = PublicInventoryItemSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'


class InventoryItemSerializer(serializers.ModelSerializer):
    """Serializer for InventoryItem model with supplier handling."""
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True
    )

    class Meta:
        model = InventoryItem
        fields = '__all__'

    def to_internal_value(self, data):
        # Convert single supplier_id to list
        supplier_ids = data.get('supplier_ids')
        if isinstance(supplier_ids, int):
            data['supplier_ids'] = [supplier_ids]
        return super().to_internal_value(data)

    def _set_suppliers(self, instance, supplier_ids):
        """Helper method to set suppliers for an instance."""
        instance.suppliers.set(Supplier.objects.filter(id__in=supplier_ids))

    def create(self, validated_data):
        """Create InventoryItem and set suppliers."""
        supplier_ids = validated_data.pop('supplier_ids')
        item = InventoryItem.objects.create(**validated_data)
        self._set_suppliers(item, supplier_ids)
        return item

    def update(self, instance, validated_data):
        """Update InventoryItem and optionally update suppliers."""
        supplier_ids = validated_data.pop('supplier_ids', None)
        instance = super().update(instance, validated_data)
        if supplier_ids is not None:
            self._set_suppliers(instance, supplier_ids)
        return instance
