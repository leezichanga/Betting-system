from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deposit(models.Model):
    name =  models.CharField(max_length=60)
    id_no = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    mobile_number = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_deposit(self):
        self.save()

    def delete_deposit(self):
        self.delete()

    @classmethod
    def get_deposit(cls):
        deposit = Deposit.objects.all()
        return deposit

    @classmethod
    def update_deposit(cls,id):
        updated = Deposit.objects.filter(id=Deposit.id).update(name=name)
        return updated

class Placebet(models.Model):
    game_id = models.CharField(max_length=60)
    amount = models.CharField(max_length=20)
    prediction = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_placebet(self):
        self.save()

    def delete_placebet(self):
        self.delete()

    @classmethod
    def get_placebet(cls):
        bet = Placebet.objects.all()
        return bet

    @classmethod
    def update_placebet(cls,id):
        updated = Placebet.objects.filter(id=Placebet.id).update(name=name)
        return updated
