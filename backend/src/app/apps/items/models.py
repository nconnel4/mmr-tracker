from django.db import models


class Item(models.Model):
    """Model for items."""

    ITEM_TYPES = [
        ("ITEM", "item"),
        ("MASK", "mask"),
        ("SONG", "song"),
        ("EQUIPMENT", "equipment"),
        ("REMAINS", "remains"),
    ]

    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    item_group = models.CharField(max_length=25)
    progress_order = models.IntegerField(default=1)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    quantity = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        db_table = "items"
        verbose_name = "item"
        verbose_name_plural = "items"
        constraints = [
            models.UniqueConstraint(
                fields=["item_group", "progress_order"], name="unique_group_progress"
            )
        ]

    def __str__(self):
        """Return item name and group."""
        return f"{self.name} [{self.code}]"
