from django import forms
from .models import Stashes, Transactions


class AddStashForm(forms.ModelForm):

	# how much do you want to save = Decimalfield()
	class Meta:
		model = Stashes
		fields = ['name_of_stash', 'discription']

class EditStashForm():
	class Meta:
		model = Stashes
		fields  = ['']


class NewStashTransactionForm(forms.ModelForm):
	class Meta:
		model = Transactions
		exclude = ['theuser', 'amount_of_stash']


class DepositMoneyTransactionForm(forms.ModelForm):
	class Meta:
		model = Transactions
		exclude = ['theuser', ]

class DepositForm(forms.Form):
	amount_of_deposit = forms.DecimalField()

	def __str__(self):
		return self.amount_of_deposit


class TransferMoneyTransactionForm(forms.ModelForm):
	pass


class WithdrawlTransactionForm(forms.ModelForm):
	pass










