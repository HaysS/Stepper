from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_allows_user_to_enter_multiple_habits(self):
		self.browser.get(self.live_server_url)
		
		self.assertIn('Stepper', self.browser.title)
		
		new_habit_elem = self.browser.find_element_by_id('new_habit')
		habit_list_table = self.browser.find_element_by_id('habit_list')
		habit_list_rows = habit_list_table.find_elements_by_tag_name('tr')

		#User enters "Brush teeth" as a new habit.
		new_habit_elem.send_keys('Brush teeth')
		new_habit_elem.send_keys(Keys.ENTER)
		#Check to see if "Brush teeth" is in the list of habits.
		self.browser.assertTrue(
			any(row.text == 'Brush teeth' for row in rows)
		)
		
