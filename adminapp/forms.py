from email import message_from_binary_file
from django import forms


# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 300px;''max_length = 50'}))
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	# email    = forms.EmailField(label='Email')
	# email.widget.attrs.update({'class':'g-col-6', 'required':'required'})
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)




# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# class Application_Form(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField(max_length = 150)
#     # age= forms.IntegerField(widget=forms.NumberInput)
#     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))


    