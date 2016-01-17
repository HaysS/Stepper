from django.shortcuts import redirect, render
from habit_lists.models import Habit, HabitList

def home_page(request):
	return render(request, 'home.html')

def view_habit_list(request):
	habits = Habit.objects.all()
	return render(request, 'habit_list.html', {'habits': habits})

def new_habit_list(request):
	habit_list_ = HabitList.objects.create()
	Habit.objects.create(text=request.POST['habit_text'], habit_list=habit_list_)
	return redirect('/habit_lists/only-habit-list/')

def view_habit_list(request):
	habits = Habit.objects.all()
	return render(request, 'habit_list.html', {'habits': habits})
