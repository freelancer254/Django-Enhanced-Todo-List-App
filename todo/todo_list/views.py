from django.shortcuts import render, redirect
from .models import List
from .form import ListForm
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

'''
@login_required means that the view wont be displayed until the user is authenticated
'''
@login_required
def home(request):
	'''
	You can add as many quotes as you want. Just needed to learn about the random module
	'''
	quotes=["You are a wonderful being","Today is your day","Simple tasks for a brilliant person",
		"An organized day is a productive day!","Started from Hello World Now You are here!"]
	if request.method =='POST':
		
		quote_of_the_day=random.choice(quotes)
		form=ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=List.objects.all
			messages.success(request,('Item has been added to list!'))
			return render(request,'home.html',{'all_items':all_items,'quote_today':quote_of_the_day})
	else:
		quote_of_the_day=random.choice(quotes)
		all_items=List.objects.all
		return render(request,'home.html',{'all_items':all_items,'quote_today':quote_of_the_day})
def delete(request,list_id):
	item= List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('item has been deleted'))

	return redirect('home')

def cross_off(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')
def uncross(request,list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')
@login_required
def edit(request, list_id):
	if request.method=='POST':
		item = List.objects.get(pk=list_id)
		form =ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ("Item has been edited!"))
			return redirect('home')

	else:
		item = List.objects.get(pk=list_id)
		return render(request,'edit.html', {'items': item})
@login_required
def email(request):
	tasks=List.objects.all().values_list('item',flat=True)
	tasks= "\n".join(tasks)
	subject = 'Your Tasks Today'
	message = ' It is good for you to complete these tasks\n '+ tasks
	email_from = 'enter sender email here'
	recipient_list = ['enter recipient email here',]
	send_mail( subject, message, email_from, recipient_list,fail_silently=False )
	messages.success(request,("Email has been sent!"))
	return redirect('home')
