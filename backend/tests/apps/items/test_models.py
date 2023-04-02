import pytest
from apps.items.models import Item
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_item_without_quantity():
    item = Item(
        code="ocarina",
        name="Ocarina of Time",
        item_group="ocarina",
        item_type="item",
    )

    assert item.code == "ocarina"
    assert item.name == "Ocarina of Time"
    assert item.item_group == "ocarina"
    assert item.progress_order == 1
    assert item.item_type == "item"
    assert not item.quantity
    assert str(item) == "Ocarina of Time [ocarina]"


@pytest.mark.django_db
def test_item_with_quantity():
    item = Item(
        code="heroBow",
        name="Hero Bow",
        item_group="bow",
        progress_order=1,
        item_type="item",
        quantity=30,
    )

    assert item.code == "heroBow"
    assert item.name == "Hero Bow"
    assert item.item_group == "bow"
    assert item.progress_order == 1
    assert item.item_type == "item"
    assert item.quantity == 30
    assert str(item) == "Hero Bow [heroBow]"


@pytest.mark.django_db
def test_item_duplicate_group_progress():
    """Database should throw error if item_group and progress_order are not unique."""
    item1 = Item(
        code="heroBow",
        name="Hero Bow",
        item_group="bow",
        progress_order=1,
        item_type="item",
        quantity=30,
    )
    item2 = Item(
        code="largeQuiver",
        name="Hero Bow",
        item_group="bow",
        progress_order=1,
        item_type="item",
        quantity=30,
    )
    item1.save()

    with pytest.raises(IntegrityError):
        item2.save()
