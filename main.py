import pyfiglet
import colorama
import subprocess
import keyboard
import os
import time
import signal
import psutil 

# Initialize colorama
colorama.init()

# Create the ASCII art text
project_name = "F-L IZZ By SD The Geek beta"
ascii_art = pyfiglet.figlet_format(project_name, font="mini")

current_process = None  # Global variable to track the subprocess

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def stop_deauth_process():
    global current_process
    if current_process and current_process.poll() is None:  # Check if process is running
        print("Stopping deauth process...")
        current_process.terminate()  # Terminate the subprocess
        current_process.wait()  # Ensure it fully stops
        print("Deauth process terminated.")
    # Kill any lingering processes related to the script
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            if "python" in proc.info["name"] and "deauth.py" in proc.cmdline():
                print(f"Killing rogue process: {proc.info['pid']}")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
def process_input(get_input):
    global current_process

    if get_input == 1:
        print("Coming Soon, After 2 seconds you will return to the main menu. Thank you!")
        time.sleep(2)
        start()
    elif get_input == 2:
        while True:
            try:
                script = "scripts/deauth.py"
                print("Press 0 to exit, 1 to go back to the main menu")
                interface = input("Please input monitored mode interface to deauth WiFi networks (e.g wlan0mon): > ")
                if interface == "0":
                    print("Thanks for using Flizz -SD")
                    stop_deauth_process()
                    exit()
                elif interface == "1":
                    stop_deauth_process()
                    start()
                mac = input("Please input target MAC address: > ")
                ch = input("Please input target channel: > ")

                # Start the deauth script
                print("Starting deauth attack. Press 'q' to stop.")
                current_process = subprocess.Popen(
                    ['python', script, interface, mac, ch],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

                while True:
                    if keyboard.is_pressed('q'):  # Stop deauth when 'q' is pressed
                        stop_deauth_process()
                        start()
                        break

            except subprocess.CalledProcessError as e:
                print(f"Error running {script}: {e.stderr}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                time.sleep(2)
                start()

    elif get_input == 3:  # WiFi Discovery
        while True:
            try:
                script = "scripts/discover-wifi.py"
                print("Press 0 to exit, 1 to go back to the main menu")
                interface = input("Please input monitored mode interface to discover WiFi networks (e.g wlan0mon): > ")
                if interface == "0":
                    print("Thanks for using Flizz -SD")
                    stop_deauth_process()
                    exit()
                elif interface == "1":
                    stop_deauth_process()
                    reset_adapter(interface)
                    start()

                # Run the discovery script
                result = subprocess.Popen(
                    ['python', script, interface],
                    stderr=subprocess.DEVNULL
                )

                print("WiFi discovery script is running. Press 'q' to stop.")
                while True:
                    if keyboard.is_pressed('q'):  # Stop with 'q'
                        result.terminate()
                        print("Process terminated.")
                        start()
                        break

            except subprocess.CalledProcessError as e:
                print(f"Error running {script}: {e.stderr}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                time.sleep(2)
                start() 
     
    elif get_input == 0:
        print("Thanks for using Flizz -SD")
        stop_deauth_process()  # Ensure subprocess is terminated
        exit()

    else:
        print("Please select a valid option, wait for 2 seconds. Thank you!")
        time.sleep(2)
        start()

def start():
    while True:
        try:
            clear_screen()
            print(f"{colorama.Fore.LIGHTRED_EX}{ascii_art}{colorama.Style.RESET_ALL}")
            print("1 for WiFi RickRoll, 2 for WiFi Deauth/Jam, 3 To Discover Wifi,  0 to Quit")
            get_input = int(input("Choose an option (e.g 1): > "))
        except ValueError:
            print("Please enter a valid number. Wait for 2 seconds. Thank you!")
            time.sleep(2)
            continue
        process_input(get_input)
        break

start()
