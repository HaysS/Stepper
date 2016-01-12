from django.shortcuts import redirect, render
from habit_lists.models import Habit

def home_page(request):
	if request.method == 'POST':
		Habit.objects.create(text=request.POST['habit_text'])
		return redirect('/')

	habits = Habit.objects.all()
	return render(request, 'home.html', {'habits': habits})
