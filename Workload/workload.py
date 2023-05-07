import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Number of clients to be connected
number_of_users = 50

# Room code of the server
room_id = "H4R0MP"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

# Provide the client landing page link here
#driver.get("http://127.0.0.1:5501/index.html")
driver.get("https://himanshu0998.github.io/watch-party/")

# Running Workload
print("Running Workload")
for i in range(1, number_of_users):
    if i > 1:
        driver.execute_script("window.open('https://himanshu0998.github.io/watch-party/');")
        driver.switch_to.window(driver.window_handles[i-1])

    driver.find_element(By.ID, "joinPartyRoomButton").click()
    joinee_name = driver.find_element(By.ID, "jName")
    joinee_name.send_keys(f"User{i}")
    party_room_id = driver.find_element(By.ID, "rId")
    party_room_id.send_keys(room_id)
    driver.find_element(By.ID, "newRoomJoinee").click()

for i in range(1, number_of_users):
    driver.switch_to.window(driver.window_handles[i-1])
    time.sleep(1)

#driver.quit()
