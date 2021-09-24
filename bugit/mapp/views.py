from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import TestMod


def mainpage (requests):
	return render(requests, 'main_page.html')


def registerr (requests):
	if requests.method == 'POST':
		regform = RegistrationForm(requests.POST)
		if regform.is_valid():
			regform.save()
			return redirect('login')
	else:
		regform = RegistrationForm()
	
	return render(requests, 'registerr.html', {'regform':regform})


def contactus(requests):
	return render(requests, 'contact_us.html')

def aboutus(requests):
	return render(requests, 'about_us.html')


# def pageonee (requests):
# 	if requests.method == 'POST':

# 		formone = TestForm(requests.POST)
# 		new_tm = TestMod(words=requests.POST['words'])
# 		new_tm.save()
# 		print(requests.POST['words'])
# 		return redirect ('mainpageview')
# 	else:
# 		formone = TestForm()

# 	return render(requests, 'pageonee.html', {'formone': formone})