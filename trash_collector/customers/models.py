from django.db import models
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=75, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    balance = models.IntegerField(null=True)
    weekly_pickup = models.CharField(max_length=15, null=True)
    one_time_pickup = models.DateField(null=True)
    suspend_start = models.DateField(null=True)
    suspend_end = models.DateField(null=True)

    def __str__(self):
        return self.name