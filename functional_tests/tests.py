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
		
