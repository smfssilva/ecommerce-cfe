from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm


def home_page(request):
	context = {
		"titulo": "This is the home page",
		"premium_content": "YEAHHHHHHHH"
	}
	return render(request, "home_page.html", context)


def about_page(request):
	context = {
		"titulo": "This is the about page"
	}
	
	return render(request, "home_page.html", context)


def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"titulo": "This is the contact page",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == 'POST':
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))

	return render(request, "contact/view.html", context)


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in")
	# print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(user)
		# print(request.user.is_authenticated)
		if user is not None:
			# print(request.user.is_authenticated)
			login(request, user)
			# context["form"] = LoginForm()
			return redirect("/login")
		else:
			print("Error")


	return render(request, "auth/login.html", context)


def register_page(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "auth/register.html", {})
