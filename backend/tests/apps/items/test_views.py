import pytest


@pytest.mark.django_db
def test_get_all_items(client, add_item):
    item_one = add_item(
        code="ocarina", name="Ocarina of Time", item_group="ocarina", item_type="item"
    )
    item_two = add_item(
        code="kokiriSword",
        name="Kokiri Sword",
        item_group="sword",
        item_type="equipment",
    )

    resp = client.get("/api/items/")
    assert resp.status_code == 200
    assert resp.data[0]["code"] == item_one.code
    assert resp.data[1]["code"] == item_two.code
