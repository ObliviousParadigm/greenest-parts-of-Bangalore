# While this code is not perfect, it certainly helps one make the computer
# do most of the work and reduce human labour. 
# The screenshots that have been captured here are stored as .png files
# The issue faced is that it occupies a lot of space(about 11.3GB). In order
# for us to be able to upload it and work with it, we decided to convert it 
# to .jpg format using Linux's command line tool imagemagick
# Commands used are as follows
# sudo apt install imagemagick
# mogrify -format jpg *.png
# rm *.png
# Doing this helped us reduce the size from 11.3GB to 1.8GB

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep
import os

os.chdir('Pics')

url = 'https://www.google.com/maps'

# options = webdriver.FirefoxOptions()
# Run Firefox normally, minus any visible UI components.
# options.add_argument('--headless')
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

searchBox = driver.find_element(By.ID, 'searchboxinput')

driver.implicitly_wait(10)

satelliteView = driver.find_element(By.CLASS_NAME, 'widget-minimap-shim-button')
satelliteView.click()

location = ['pes university', 'Kempegowda', 'Chowdeshwari', 'Attur', 'Yelahanka Satellite Town', 'Jakkur', 'Thanisandra', 'Byatarayanapura', 'Kodigehalli', 'Vidyaranyapura', 'Doddabommasandra', 'Kuvempu Nagar', 'Shettyhalli', 'Mallasandra', 'Bagalagunte', 'T-Dasarahalli', 'Jalahalli', 'J.P.Park', 'Radhakrishna Temple', 'Sanjay Nagar', 'Hebbal', 'Vishwanathnagenahalli', 'Nagavara', 'HBR Layout', 'Horamavu', 'Ramamurthy Nagar', 'Banaswadi', 'Kammanahalli', 'Kacharakanahalli', 'Kadugondanahalli', 'Kushal Nagar', 'Kavalbyrasandra', 'Manorayanapalya', 'Gangenahalli', 'Aramane Nagar', 'Mathikere', 'Yeshwanthpur', 'H.M.T', 'Chokkasandra', 'Dodda Bidarkallu', 'Peenya Industrial Area', 'Lakshmidevi Nagar', 'Nandini Layout', 'Marappana Palya', 'Malleshwaram', 'Jayachamarajendra Nagar', 'Devarajeevanahalli', 'Muneshwara Nagar', 'Lingarajapuram', 'Benniganahalli', 'Vijanapura', 'K.R.Puram', 'Basavanapura', 'Hoodi', 'Devasandra', 'A.Narayanapura', 'C.V.Raman Nagar', 'Hosathippasandra', 'Maruthiseva Nagar', 'Sagayapuram', 'S.K.Garden', 'Ramaswamy Palya', 'Jayamahal', 'Subramanya Nagar', 'Nagapura', 'Mahalakshmipuram', 'Laggere', 'Rajagopala Nagar', 'Hegganahalli', 'Herohalli', 'Kottigepalya', 'Shakthiganapathi Nagar', 'Shankaramata', 'Gayathri Nagar', 'Pulikeshi Nagar', 'Sarvagna Nagar', 'Hoysala Nagar', 'Vignana Nagar', 'Garudacharpalya', 'Kadugudi', 'Hagadooru', 'Doddanekkundi', 'Marathalli', 'HAL Airport', 'Jeevanbhima Nagar', 'Jogupalya', 'Ulsoor', 'Bharathi Nagar', 'Shivaji Nagar', 'Vasanth Nagar', 'Subhash Nagar', 'Okalipuram', 'Dayananda Nagar', 'Prakash Nagar', 'Rajaji Nagar', 'Basaveshwara Nagar', 'Kamakshipalya', 'Kaveripura', 'Govindraja Nagara', 'Agrahara Dasarahalli', 'Shiva Nagar', 'Chickpete', 'Sampangiram Nagar', 'Shanthala Nagar', 'Domlur', 'Konena Agrahara', 'Agaram', 'Vannarpet', 'Neelasandra', 'Shanthi Nagar', 'Sudam Nagar', 'Dharmarayaswamy Temple Ward', 'Cottonpet', 'Binnipet', 'Kempapura Agrahara', 'Vijay Nagar', 'Hosahalli', 'Marenahalli', 'Moodalapalya', 'Nagarabhavi', 'Jnanabharathi Ward', 'Nayandanahalli', 'Attiguppe', 'Hampi Nagar', 'Bapuji Nagar', 'Jagareevanram Nagar', 'Rayapuram', 'Chalavadipalya', 'K.R.Market', 'Chamrajpet', 'Azad Nagar', 'Sunkenahalli', 'Visvesvarapuram', 'Siddapura', 'Adugodi', 'Ejipura', 'Varthur', 'Bellandur', 'Koramangala', 'Sudduguntepalya', 'Jayangar', 'Basavanagudi', 'Hanumantha Nagar', 'Sri Nagar', 'Gali Anjaneya Swamy Temple Ward', 'Deepanjali Nagar', 'Kengeri', 'Rajarajeshwari Nagar', 'Hosakerehalli', 'Giri Nagar', 'Katriguppe', 'Vidyapeetha', 'Ganeshmandira Ward', 'Karisandra', 'Yadiyuru', 'Pattabhiram Nagar', 'Byrasandra', 'Jayanagar East', 'Gurappanapalya', 'Madiwala', 'Jakkasandra', 'HSR Layout', 'Bommanahalli', 'BTM Layout', 'J.P.Nagar', 'Sarakki', 'Shakambari Nagar', 'Banashankari Temple Ward', 'Kumaraswamy Layout', 'Padmanabha Nagar', 'Chikkalasandra', 'Uttarahalli', 'Yelachenahalli', 'Jaraganahalli', 'Puttenahalli', 'Bilekahalli', 'Hongasandra', 'Mangammanapalya', 'Singasandra', 'Begur', 'Arakere', 'Gottigere', 'Konanakunte', 'Anjanapur', 'Vasanthapura', 'Hemmigepur']

# COULD NOT FIND 'Rajamahal', 'Kadumalleshwara', 'Dattathreya Temple', 'Gandhi Nagar', 'Vrushabhavathi', 'Dr.Rajkumar Ward', 'Sri Rammandira', 'Maruthi Mandira Ward', 'Ullalu', 'Padarayanapura', 'Lakkasandra', 

locations = [i+', Bangalore' for i in location]

for place in locations:
	searchBox.clear()
	searchBox.send_keys(place)
	searchBox.send_keys(Keys.ENTER)

	sleep(5)

	collapseSearch = driver.find_element(By.XPATH, '/html/body/jsl/div[3]/div[9]/div[8]/div/div[3]')
	collapseSearch.click()

	# Finding the draggable element
	canvas = driver.find_element(By.CLASS_NAME, 'widget-scene-canvas')

	# Define ActionChains
	actions = ActionChains(driver)

	zoom = driver.find_element(By.CLASS_NAME, 'widget-zoom-in')
	zoom.click()

	# collapseSearch.click()
	for a in range(2):
		name = place
		for b in range(2):
			print('left')
			driver.save_screenshot("{name}{a}{b}.png".format(name = name, a = a, b = b))
			actions.drag_and_drop_by_offset(canvas, 100, 0)
			actions.perform()
			# actions.move_by_offset(-100, 0)
			# actions.perform()

		driver.save_screenshot("{name}UP{a}.png".format(name = name, a = a))
		actions.drag_and_drop_by_offset(canvas, 0, 100)
		actions.perform()
		# actions.move_by_offset(0, -100)
		# actions.perform()

		for c in range(2):
			driver.save_screenshot("{name}{a}{c}.png".format(name = name, a = a+1, c = c))
			actions.drag_and_drop_by_offset(canvas, -100, 0)
			actions.perform()
			# actions.move_by_offset(-100, 0)
			# actions.perform()

		driver.save_screenshot("UP.png")
		actions.drag_and_drop_by_offset(canvas, 0, 100)
		actions.perform()

	collapseSearch.click()

driver.quit()