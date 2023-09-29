import random
import pywhatkit
import time
import pyautogui
from datetime import datetime

# Initializing number and message
recipient_number = "+14372695669"
message = "Good Morning!"

# Initializing variables with time
send_hour = 9 
send_minute = random.randint(1,58)

while True:
    # Get the current date and time
    now = datetime.now()

    # Check if it's the desired time to send the message
    if now.hour == send_hour and now.minute == send_minute:
        # Send the message using pywhatkit
        pywhatkit.sendwhatmsg(recipient_number, message, now.hour, now.minute + 1)  

        # Wait for a few seconds to ensure the message is sent
        time.sleep(5)

        # Simulate clicking the somewhere in the tab to bring the cursor to the text box
        pyautogui.click(1050, 950)
        # Sleep for 2 seconds to ensure time to load
        time.sleep(2)
        # Press enter key to send message
        pyautogui.press('enter')
        # Sleep for 2 seconds to ensure message is sent
        time.sleep(2)
        #Close the window
        pyautogui.hotkey('command', 'w')

        # Sleep for a day to avoid sending multiple messages on the same day
        time.sleep(86400) 
    else:
        # Sleep for a minute and check again
        time.sleep(60)
        
