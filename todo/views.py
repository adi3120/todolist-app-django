from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Todo
from datetime import datetime
# Create your views here.
def index(request):
	todo=Todo.objects.all()

	if request.method=='POST':
		new_todo=Todo(
			title=request.POST["title"],
			date=datetime.now()
		)
		new_todo.save()
		return redirect('/todo')
		 
	return render(request,'todo/index.html',{'todo':todo})

def delete(request,pk):
	todo=Todo.objects.get(id=pk)
	todo.delete()
	return redirect('/todo')

	
