import pytest
from apps.items.models import Item


@pytest.fixture(scope="function")
def add_item():
    def _add_item(
        code: str,
        name: str,
        item_group: str,
        item_type: str,
        progress_order: int = 1,
        quantity: int | None = None,
    ):
        item = Item.objects.create(
            code=code,
            name=name,
            item_group=item_group,
            item_type=item_type,
            progress_order=progress_order,
            quantity=quantity,
        )
        return item

    return _add_item
