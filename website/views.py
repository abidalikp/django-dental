from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'index.html', {})

def contact(request):

	if request.method == 'POST':
		# Get From Data
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send Email
		send_mail(
			message_name,#subject
			message,#message
			message_email,#from
			['abidalikp122@gmail.com'],#to
			fail_silently=False,
		)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})
