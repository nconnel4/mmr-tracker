import pytest
from apps.items.serializers import ItemSerializer


@pytest.mark.django_db
def test_valid_item_serializer():
    valid_item = {
        "code": "ocarina",
        "name": "Ocarina of Time",
        "item_group": "ocarina",
        "progress_order": 1,
        "item_type": "ITEM",
        "quantity": None,
    }
    serializer = ItemSerializer(data=valid_item)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_item
    assert serializer.data == valid_item
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_item_serializer():
    invalid_item = {
        "code": "ocarina",
        "name": "Ocarina of Time",
        "item_group": "ocarina",
        "progress_order": 1,
    }
    serializer = ItemSerializer(data=invalid_item)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_item
    assert serializer.errors == {"item_type": ["This field is required."]}
