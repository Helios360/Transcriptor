from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from openai import OpenAI
import pyautogui
import numpy as np
import random
import time
import os
import whisper

# modify the login and paswword in the login function
# modify the path of creation of the record if you want
# modify the openAI api key
# modify the XPATH for the id of the discord room
# ----------- :3 THANK YOU <3 --------------------

model = whisper.load_model("medium") # you can set a more performant model for better pc

options = Options()
options.headless = False
gecko_path = "/home/user/Programs/AutomateThis/geckodriver"
options.binary_location = "/usr/bin/firefox"
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

    for i in range(num_steps):
        jitter_factor = random.uniform(-4, 4)
        if i > num_steps * 0.8:
            jitter_factor *= 0.5
        x_coords[i] += jitter_factor
        y_coords[i] += jitter_factor

        progress = i / num_steps
        easing = progress * (2 - progress)
        smooth_x = start_x + (end_x - start_x) * easing
        smooth_y = start_y + (end_y - start_y) * easing

        pyautogui.moveTo(smooth_x, smooth_y)
        time.sleep(random.uniform(0.015, 0.03))

def login():
    time.sleep(2)
    pyautogui.write("YOUR DISCORD LOGIN")
    pyautogui.press("tab")
    pyautogui.write("YOUR DISCORD PASSWORD")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    print("Please do the captcha yourself !!! >w<")
    input("Please wait, discord is loading :3 ...")
    move_mouse_human_like(600, 600, 15, 282, duration=1) #modify coords to where the server button is
    pyautogui.click()

def main():
    action = input("Action: 1=Transcript_discord 2=truc 3=truc\n")
    if action == "1":
        login()
        room = driver.find_element(By.XPATH, '') #path to discord room
        room.click()
        os.system("./recorder2.sh")
    else:
        print("No good option was selected, try again :3")
        print("Exiting ...")
        return

    input("Press Enter to exit...")
    result = model.transcribe("/home/user/Documents/output.wav", language="fr")
    print(result["text"])
    transcript = result["text"]
    driver.quit()

    client = OpenAI(api_key="YOUR API KEY HERE")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
		   "Tu es un assistant utile chargé de résumer des transcriptions audio en français. "
		   "Ces transcriptions sont générées localement avec Whisper, ce qui peut entraîner des imprécisions, "
		   "notamment lorsque l'interlocuteur bafouille ou parle de manière peu claire. "
		   "Les transcriptions concernent des réunions d'information destinées à des élèves intéressés par une inscription à Cloud Campus. "
		   "Il arrive également que des élèves prennent la parole pour poser des questions ou partager leurs expériences. "
		   "Ton résumé doit être clair, concis et adapté à un public de futurs étudiants."
	   )},
            {"role": "user", "content": f"Peux-tu résumer ceci : {transcript}"}
        ],
        temperature=0.7,
        max_tokens=400
    )
    summary = response.choices[0].message.content
    print("Résumé en français:\n", summary)

main()
