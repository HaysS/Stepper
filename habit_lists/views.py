from django.shortcuts import redirect, render
from habit_lists.models import Habit, HabitList

def home_page(request):
	return render(request, 'home.html')

def view_habit_list(request, habit_list_id):
	habit_list_ = HabitList.objects.get(id=habit_list_id)
	habits = Habit.objects.filter(habit_list=habit_list_)
	return render(request, 'habit_list.html', {'habit_list': habit_list_})

def new_habit_list(request):
	habit_list_ = HabitList.objects.create()
	Habit.objects.create(text=request.POST['habit_text'], habit_list=habit_list_)
	return redirect('/habit_lists/%d/' % (habit_list_.id,))

def add_habit(request, habit_list_id):
	habit_list_ = HabitList.objects.get(id=habit_list_id)
	habit = Habit.objects.create(text=request.POST['habit_text'], habit_list=habit_list_)
	return redirect('/habit_lists/%d/' % (habit_list_.id,)) 
