from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, random, csv

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rock-paper-scissors-tau-two.vercel.app/gamePage")

# CSV
data_header = [
    ["Bot Pick", "Computer Pick", "Bot Result", "Computer Result"]
]

with open("dataset_2.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data_header)

# Loop for functionality
for i in range(1000):
    # Get Elements
    rock = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/button")
    paper = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/button")
    scissors = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button")
    weapons = {"ROCK": rock, "PAPER": paper, "SCISSORS": scissors}

    # Randomise Bot's Pick
    random_key = random.choice(list(weapons.keys()))  # Get a random key
    bot_weapon_pick = weapons[random_key].click()  # Click the value
    bot_weapon_pick_string = random_key

    # Store Site Computer's Pick and Result
    computer_pick = driver.find_element(By.XPATH, "/html/body/div[3]/h1[1]").text.split(" ")[-1]
    bot_result = driver.find_element(By.CLASS_NAME, "winOrLoseText").text.split(" ")[-1]
    computer_result = ""

    if (bot_result == 'Win'):
        computer_result = 'Loss'
    elif (bot_result == 'Lose'):
        computer_result = 'Win'
        bot_result = 'Loss'
    else:
        computer_result = 'Tie'

    # CSV Appending
    with open("dataset_2.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bot_weapon_pick_string, computer_pick, bot_result, computer_result])

    # Restart game
    restart_button = driver.find_element(By.LINK_TEXT, "Restart").click()


driver.quit()