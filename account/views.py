from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import  logout
from random import seed, randint
from django.core.mail import send_mail
import sendgrid
import os

from .forms import *
from .controllers import *
from .models import Client

class IndexView(View):
	form_class = IndexForm
	template_name = 'account/reg.html'
	controller = IndexController
	def get(self, request):
		client = self.request.user
		if client.is_authenticated:
			return redirect('home:Homepage')
		form = self.form_class(None)
		return render(request=request, template_name=self.template_name, context={'form' : form})
	def post(self, request):
		form = self.form_class(request.POST)
		controller = self.controller
		if form.is_valid():
			idNo = form.cleaned_data['idNo']
			request.session['idNo'] = idNo
			if controller.verifyIdNewUser(idNo):
				return redirect('account:Register')
			return redirect('account:Signin')
		return render(request=request, template_name=self.template_name, context={'form' : form})

class RegistrationView(View):
	form_class = RegistrationForm
	controller = RegistrationController
	template_name = 'account/reg_fin.html'

	def get(self, request):
		idNo = self.request.session.get('idNo')
		client = self.request.user
		if client.is_authenticated:
			return redirect('home:Homepage')
		if idNo == None:
			return redirect('account:Index')
		if IndexController.verifyIdNewUser(idNo) == False:
			return redirect('account:Signin')
		form = self.form_class(None)
		return render(request=request, template_name=self.template_name, context={'form': form, 'idNo' : idNo})
	def post(self, request):
		form = self.form_class(request.POST)
		controller = self.controller
		if form.is_valid():
			idNo = self.request.session['idNo']
			password = form.inputDetails().get('password')
			firstName = form.getFNameTxt()
			lastName = form.getLNameTxt()
			email = form.inputDetails().get('email')
			result = controller.saveUserAndLogin(request, idNo, password, firstName, lastName, email)
			if result:
				return redirect('home:Homepage')
		return render(request, self.template_name, {'form' : form})


class LoginView(View):
	form_class = LogInForm
	template_name = 'account/reg_fin.html'
	def get(self, request):
		idNo = request.session.get('idNo')
		if idNo == None:
			return redirect('account:Index')
		if IndexController.verifyIdNewUser(idNo):
			return redirect('account:Register')
		form = self.form_class(None)
		return render(request=request, template_name=self.template_name, context={'form': form, 'idNo' : idNo})
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			idNo = request.session['idNo']
			password = request.POST['password']
			user = Client.objects.get(username=idNo)
			user = authenticate(username=idNo, password=password)
			if user is not None:
				login(request, user)
				print(request.user.username + " @Login")
				return redirect('home:Homepage')
			if Client.objects.get(username=idNo).is_active == 0:
				return render(request=request, template_name=self.template_name, context={'form' : form, 'idNo' : idNo,  'error_message' : 'Your account is locked.'})
		return render(request=request, template_name=self.template_name, context={'form' : form, 'idNo' : idNo,  'error_message' : 'Incorrect password.'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:Index')

class ForgetPasswordView(View):
	form_class = ForgetPasswordForm
	template_name = 'account/forget_pw.html'
	def get(self, request):
		idNo = request.session.get('idNo')
		if idNo == None:
			return redirect('account:Index')
		user = Client.objects.get(username=idNo)
		if user.first_name == "":
			return redirect('account:Register')
		user.verificationCode = randint(10000, 99999)
		user.save()
		res = send_mail('Reset Password', 'Here is your verification code: ' + str(user.verificationCode), 'wildcatinnolabs@gmail.com', [user.email], fail_silently=False)
		#sg = sendgrid.SendGridAPIClient('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')
#		data = {
#		  "personalizations": [
#		    {
#		      "to": [
#		        {
#		          "email": user.email
#		        }
#		      ],
#		      "subject": 'Here is your verification code: ' + str(user.verificationCode)
#		    }
#		  ],
#		  "from": {
#		    "email": "wildcatslab@yahoo.com"
#		  },
#		  "content": [
#		    {
#		      "type": "text/plain",
#		      "value": "Reset Password"
#		    }
#		  ]
#		}
#		response = sg.client.mail.send.post(request_body=data)
#		print(response.status_code)
#		print(response.body)
#		print(response.headers)
		form = self.form_class(None)
		return render(request=request, template_name=self.template_name, context={'form' : form, 'idNo' : idNo})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			idNo = request.session['idNo']
			verifCode = form.cleaned_data['verificationCode']
			request.session['verifCode'] = verifCode
			user = Client.objects.get(username=idNo)
			if user.verificationCode == verifCode:
				return redirect('account:ChangePassword')
		return render(request=request, template_name=self.template_name, context={'form' : form, 'idNo' : idNo,  'error_message' : 'Code does not match'})


class ChangePasswordView(View):
	form_class = ChangePasswordForm
	template_name = 'account/reg_fin.html'
	def get(self, request):
		idNo = request.session.get('idNo')
		if idNo == None:
			return redirect('account:Index')
		user = Client.objects.get(username=idNo)
		verifCode = request.session.get('verifCode')
		form = self.form_class(None)
		if user.verificationCode == verifCode:
			return render(request=request, template_name=self.template_name, context={'form' : form, 'idNo' : idNo})
		return redirect('account:ForgetPassword')

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			idNo = request.session.get('idNo')
			password = form.cleaned_data['password']
			conf_password = form.cleaned_data['conf_password']
			user = Client.objects.get(username=idNo)
			user.set_password(password)
			user.verificationCode = ""
			user.save()
			if user is not None:
				login(request, user)
				return redirect('home:Homepage')
		return render(request, self.template_name, {'form' : form})
