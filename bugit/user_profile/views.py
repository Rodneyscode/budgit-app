from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import AddStashForm, NewStashTransactionForm, DepositForm
from .models import Transactions, Stashes

# Create your views here.
@login_required
def profilee(requests):

	context = {'rr':Stashes.objects.filter(theuser=requests.user),
									 'none':None, 'blank':''}

	return render(requests, 'profilee.html', context)


def addmoney(requests):
	if requests.method == 'POST':
		depform = DepositForm(requests.POST)
		if depform.is_valid():
			pass
			
	return render(requests, 'deposit.html')
	


def stashone (requests):

	stashlist = Stashes.objects.filter(theuser=requests.user)
	firststash = stashlist[0]
	context = {'firststash':firststash}

	return render(requests, 'firststash.html', context)



def stashtwo (requests):
	stashlist = Stashes.objects.filter(theuser=requests.user)
	secondstash = stashlist[1]
	context = {'secondstash': secondstash} 

	return render(requests, 'secondstash.html', context)


def stashthree (requests):
	stashlist = Stashes.objects.filter(theuser=requests.user)
	thirdstash = stashlist[2]
	context = {'thirdstash': thirdstash}

	return render(requests, 'thirdstash.html', context)


def stashfour (requests):
	stashlist = Stashes.objects.filter(theuser=requests.user)
	fourthstash = stashlist[3]
	context = {'fourthstash': fourthstash}

	return render(requests, 'fourthstash.html', context)


def stashfive (requests):
	stashlist = Stashes.objects.filter(theuser=requests.user)
	fifthstash = stashlist[4]
	context = {'fifthstash': fifthstash}

	return render(requests, 'fifthstash.html', context)



@login_required
def transactions(requests):

	context = {'tt': Transactions.objects.filter(theuser=requests.user)}

	return render(requests, 'transactions.html', context)



@login_required
def addastash(requests):
	if requests.method == "POST":
		addingtostash = AddStashForm(requests.POST)
		addingtotrans = NewStashTransactionForm(requests.POST)
		if addingtostash.is_valid():

			amountt = requests.POST['amount_of_stash']
			newstash = addingtostash.save(commit=False)
			newtrans = addingtotrans.save(commit=False)
			newstash.theuser = requests.user
			newtrans.theuser = requests.user
			newstash.save()
			newtrans.save()
			return redirect('profilee')
	else:
		addingtostash = AddStashForm()
	


	context = {'addingtostash': addingtostash}
	
	return render(requests, 'createstash.html', context )




@login_required
def transferfunds(requests):
	return render(requests, 'transfers.html')

# SETTINGS PAGE --------------------------------

@login_required
def settingspage(requests):

	return render(requests, 'settingspage.html')

@login_required
def editprofile (requests):
	
	return render(requests, 'editprofile.html')

@login_required
def updateprofile():
	pass

@login_required
def bankinginfo (requests):

	return render(requests, 'bankinginfo.html')


@login_required
def editastash(requests):

	context = {'rr':Stashes.objects.filter(theuser=requests.user),
									 'none':None, 'blank':''}

	return render(requests, 'editastash.html', context)

@login_required
def changepassword (requests):
	pass

@login_required
def editstash(requests):

	# edit = EditStashForm(requests.POST)
	# return render(requests, 'edits.html')
	pass

@login_required
def deletestash(requests):
	pass
