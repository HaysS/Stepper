from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from habit_lists.models import Habit
from habit_lists.views import home_page

class HomePageTest(TestCase):
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class HabitModelTest(TestCase):

	def test_saving_and_retrieving_habits(self):
		first_habit = Habit()
		first_habit.text = 'The first habit'
		first_habit.save()

		second_habit = Habit()
		second_habit.text = 'The second habit'
		second_habit.save()

		saved_habits = Habit.objects.all()
		self.assertEqual(saved_habits.count(), 2)

		first_saved_habit = saved_habits[0]
		second_saved_habit = saved_habits[1]
		self.assertEqual(first_saved_habit.text, 'The first habit')
		self.assertEqual(second_saved_habit.text, 'The second habit')

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		response = self.client.get('/habit_lists/only-habit-list/')
		self.assertTemplateUsed(response, 'habit_list.html')	

	def test_home_page_displays_all_habits(self):
		Habit.objects.create(text='habit 1')
		Habit.objects.create(text='habit 2')
		
		response = self.client.get('/habit_lists/only-habit-list/')

		self.assertContains(response, 'habit 1')
		self.assertContains(response, 'habit 2')

class NewListTest(TestCase):

	def test__can_save_a_POST_request(self):
		self.client.post(
			'/habit_lists/new',
			data={'habit_text': 'A new habit'}
		) 		
		self.assertEqual(Habit.objects.count(), 1)
		new_habit = Habit.objects.first()
		self.assertEqual(new_habit.text, 'A new habit')

	def test_redirects_after_POST(self):
		response = self.client.post(
			'/habit_lists/new',
			data={'habit_text': 'A new habit'}
		) 		
		self.assertRedirects(response, '/habit_lists/only-habit-list/')


