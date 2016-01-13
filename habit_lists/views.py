from django.shortcuts import redirect, render
from habit_lists.models import Habit

def home_page(request):
	return render(request, 'home.html')

def view_habit_list(request):
	habits = Habit.objects.all()
	return render(request, 'habit_list.html', {'habits': habits})

def new_habit_list(request):
	Habit.objects.create(text=request.POST['habit_text'])
	return redirect('/habit_lists/only-habit-list/')
