from django.db import models
from Custemer.models import Custemer
from Products.models import Product 

# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    CART_SATGE=0
    ORDER_CONFIRM=1
    ORDER_PROCESSED=2
    ORDER_DELIVERD=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                   (ORDER_DELIVERD,'ORDER_DELIVERD'),
                   (ORDER_REJECTED,'ORDER_REJECTED'))
    Owner=models.ForeignKey(Custemer,on_delete=models.SET_NULL,null=True,related_name='Order')
    Total_price=models.FloatField(default=0)
    Order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_SATGE)
    Delete_Status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    Created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__ (self) -> str:
        return "order-{}-{}".format(self.id, self.Owner.Name) 
    


class OrderItem (models.Model):
    Product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_cart')
    Quantity=models.IntegerField(default=1)
    Owner=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,related_name='added_item')
    def __str__ (self) -> str:
        return "order-{}-{}".format(self.id, self.Owner.Owner.Name)