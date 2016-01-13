from django.shortcuts import redirect, render
from habit_lists.models import Habit

def home_page(request):
	if request.method == 'POST':
		Habit.objects.create(text=request.POST['habit_text'])
		return redirect('/habit_lists/only-habit-list/')

	habits = Habit.objects.all()
	return render(request, 'home.html', {'habits': habits})

def view_habit_list(request):
	habits = Habit.objects.all()
	return render(request, 'home.html', {'habits': habits})
