import pyfiglet
import colorama
import subprocess
import keyboard 
import os
import time

# Initialize colorama
colorama.init()

# Create the ASCII art text
project_name = "F-L IZZ By SD The Geek --v-1"
ascii_art = pyfiglet.figlet_format(project_name, font="mini")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def process_input(get_input):
    if get_input == 1:
        print("Coming Soon, After 2 seconds you will return to main menu, Thank you")
        time.sleep(2)
        start()
    elif get_input == 2:
        while True:
            try:
                script = "scripts/deauth.py"
                print("Press 0 to exit, 1 to go back main menu")
                interface = input("Please input monitored mode interface that you want to use and deauth wifi networks with (e.g wlan0mon): > ")
                if interface == "0":
                   print("Thanks for using Flizz -SD")
                   exit()
                if interface == "1":
                   start()   
                mac = input("Please input target mac address: > ")
                ch = input("Please input target channel: > ")

                # Running the deauth script silently without capturing output
                result = subprocess.Popen(
                    ['python', script, interface, mac, ch],
                    stdout=subprocess.DEVNULL,  # Discarding the output
                    stderr=subprocess.DEVNULL   # Discarding the error
                )

                print("Deauth script is running. Press 'q' to stop.")
                while True:
                    if keyboard.is_pressed('q'):  # Check if 'q' is pressed to stop
                        result.terminate()  # Terminate the subprocess
                        start()
                        print("Process terminated. Restarting the deauth script...")
                        break  # Break and restart the process

            except subprocess.CalledProcessError as e:
                print(f"Error running {script}: {e.stderr}")
    elif get_input == 0:
        print("Thanks for using Flizz -SD")
        exit()  

    else:
        print("Please select a valid option, wait for 2 seconds, Thanks for you Patience")
        time.sleep(2)
        start()

def start():
    clear_screen()
    while True:
        try:
            print(f"{colorama.Fore.LIGHTRED_EX}{ascii_art}{colorama.Style.RESET_ALL}")
            print("1 for Wifi RickRoll, 2 for Wifi Deauth/Jam, More Option, 0 to Quit")
            print("Choose Option (e.g 1) : ")
            get_input = int(input("option here: > "))                            
        except ValueError:
            print("Please a Valid integer Number, wait for 2 seconds, Thank you")
            time.sleep(2)
            start()
        process_input(get_input)
        break
start()
