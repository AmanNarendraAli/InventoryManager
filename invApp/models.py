from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    sku = models.CharField(max_length = 50,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    class Meta: #used to specify additional options for the model, such as the name of the database table to use, ordering of query results, and other metadata
        db_table = "InventoryManager"
    def __str__(self):
        return self.product_name