from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Stashes (models.Model):
	name_of_stash = models.CharField(max_length=40)
	amount_of_stash = models.DecimalField(decimal_places=2, max_digits=6, null=True)
	discription = models.TextField(null=True)
	depositamount = models.DecimalField(decimal_places=2, max_digits=6, null=True)
	predictedgoaldate = models.DateField(null=True)
	theuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name_of_stash

class DepositInfo (models.Model):
	name_of_bank = models.CharField(max_length=100)
	accountnumber = models.IntegerField()
	routingnumber = models.IntegerField()
	paydaycycle = models.IntegerField()
	theuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name_of_bank

class Transactions(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	name_of_stash = models.CharField(max_length=40, null=True)
	amount_of_stash = models.FloatField(null=True)
	theuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	# is_new_stash = models.booleanfield()
	# amount_of_transfer = models.decimalFields()
	# withdrawl = models.booleanfield()

	def __str__(self):
		return self.name_of_stash


# class DepositTable (models.Model):
# 	depositss = models.FloatField()
# 	theuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

