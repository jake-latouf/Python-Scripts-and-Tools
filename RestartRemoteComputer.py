import wmi
import datetime
import time
import os

# Set the name of the remote computer
computer_name = "remote-computer-name"

# Get the last boot time of the remote computer
c = wmi.WMI(computer_name)
os_info = c.Win32_OperatingSystem()[0]
last_boot_time_str = os_info.LastBootUpTime.split(".")[0]
last_boot_time = datetime.datetime.strptime(last_boot_time_str, "%Y-%m-%d %H:%M:%S")
days_since_last_boot = (datetime.datetime.now() - last_boot_time).days

# Prompt the user to confirm reboot
if days_since_last_boot >= 7:
    print(f"It has been more than one week since {computer_name} was last rebooted.")
    confirmation = input("Do you want to continue? (y/n)")
    if confirmation.lower() == "y":
        print(f"{computer_name} will reboot in 5 seconds.")
        time.sleep(5)
        os.system(f"shutdown /m \\\\{computer_name} /r /f")
    else:
        exit()
elif days_since_last_boot <= 7:
    print(f"{computer_name} has been recently rebooted.")
    confirmation = input("Do you want to continue? (y/n)")
    if confirmation.lower() == "y":
        print(f"{computer_name} will reboot in 5 seconds.")
        time.sleep(5)
        os.system(f"shutdown /m \\\\{computer_name} /r /f")
    else:
        exit()
