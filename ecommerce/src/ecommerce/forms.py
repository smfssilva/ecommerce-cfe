from django import forms


class ContactForm(forms.Form):
	fullname	= forms.CharField(label='Name:', 
								widget=forms.TextInput(attrs=
									{"class":"form-control", 
									"id":"form_fullname",
									"placeholder":"Enter your name"}))
	email		= forms.EmailField(label='E-Mail:', 
								widget=forms.EmailInput(attrs={
									"class":"form-control",
									"id":"form_email",
									"placeholder":"Enter your E-mail"
									}))
	content 	= forms.CharField(label='Content:',
								widget=forms.Textarea(attrs=
									{"class":"form-control",
									"id":"form_content",
									"placeholder": "Your message"}))

	
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("E-mail has to be gmail.com")
		return email


class LoginForm(forms.Form):
	username	= forms.CharField()
	password	= forms.CharField(widget=forms.PasswordInput)