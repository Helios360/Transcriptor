from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pyautogui
import numpy as np
import random as random
import time
import os

options = Options()
options.headless = False
gecko_path = "/home/user/Programs/AutomateThis/geckodriver"
options.binary_location ="/usr/bin/firefox" 
service = Service(gecko_path)
driver = webdriver.Firefox(service=service, options=options)
driver.set_window_size(500, 500)
driver.set_window_position(-24, 0)
driver.get("https://discord.com/login")
driver.implicitly_wait(1)

def move_mouse_human_like(start_x, start_y, end_x, end_y, duration=1.0):
    num_steps = int(duration * 60)  # 60 steps per second
    x_coords = np.linspace(start_x, end_x, num_steps)
    y_coords = np.linspace(start_y, end_y, num_steps)

    # Adding some slight acceleration and deceleration
    for i in range(num_steps):
        # Random jitter, but adjust based on how far we've moved
        jitter_factor = random.uniform(-4,4)
        # Introduce more randomization closer to the destination
        if i > num_steps * 0.8:
            jitter_factor *= 0.5  # Less jitter when we're near the destination
        x_coords[i] += jitter_factor
        y_coords[i] += jitter_factor

        # Slight easing for smoother transitions
        progress = i / num_steps
        easing = progress * (2 - progress)  # Ease-in, ease-out function
        smooth_x = start_x + (end_x - start_x) * easing
        smooth_y = start_y + (end_y - start_y) * easing

        pyautogui.moveTo(smooth_x, smooth_y)
        time.sleep(random.uniform(0.015, 0.03))  # Add randomness to delay for human-like behavior
"""
def move_mouse_human_like(start_x, start_y, end_x, end_y, duration=1.0):
        num_steps = int(duration * 240)  # 60 steps per second (you can adjust this)
        x_coords = np.linspace(start_x, end_x, num_steps)
        y_coords = np.linspace(start_y, end_y, num_steps)
        for i in range(num_steps):
                if(i%random.randint(9,11) == 0):
                        offset_x = random.uniform(-2, 2)
                        offset_y = random.uniform(-2, 2)
                x_coords[i] += offset_x
                y_coords[i] += offset_y
                pyautogui.moveTo(x_coords[i], y_coords[i])
pyautogui.moveTo(1000,1000,duration=2)
"""


#move_mouse_human_like(100, 100, 500, 500, duration=1)

def login():
	os.system("setxkbmap us")
	time.sleep(2)
	pyautogui.write("DISCORD ACCOUNT'S EMAIL ADDRESS")
	pyautogui.press("tab")
	pyautogui.write("DISCORD ACCOUNT'S PASSWORD")
	pyautogui.press("tab")
	pyautogui.press("tab")
	pyautogui.press("enter")
	print("Please do the captcha yourself !!! >w<")
	input("Please wait, discord is loading :3 ...")
	move_mouse_human_like(600,600,15,282, duration=1)
	pyautogui.click()
	os.system("setxkbmap fr")

def main():
	action=input("Action: 1=Transcript_discord 2=truc 3=truc\n")
	if action=="1":
		login()
		room = driver.find_element(By.XPATH,'//*[@data-list-item-id="channels___1364598878623502339"]')
		room.click()
		os.system("./recorder2.sh")
	else :
		print("No good option was selected, try again :3")
		print("Exiting ...")
	input("Press Enter to exit...")
	driver.quit()
main()
