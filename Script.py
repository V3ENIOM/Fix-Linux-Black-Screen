import subprocess
import time
user_input=int(input("What display manager you prefer in the user login interface?!\n 1: GNOME  \n 2: KDE  \n "))
if user_input == 1:
    command = "cd ~"
    subprocess.run(["sudo", "apt-get", "install", "gdm3","-y"])
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "service", "gdm3", "stop"])
    subprocess.run(["Xorg", "-configure"])
    subprocess.run(["sudo", "cp", "xorg.conf.new", "/etc/X11/xorg.conf"])
    print("DONE, MADE WITH LOVE, V3ENIOM")
    time.sleep(3)
    subprocess.run(["sudo", "service", "gdm3", "start"])
    subprocess.run(["sudo","reboot","-f"])
elif user_input == 2:
    subprocess.run(["sudo", "apt", "install", "lightdm","-y"])
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "service", "lightdm", "stop"])
    subprocess.run(["Xorg", "-configure"])
    subprocess.run(["sudo", "cp", "xorg.conf.new", "/etc/X11/xorg.conf"])
    print("DONE, MADE WITH LOVE, V3ENIOM")
    time.sleep(3)
    subprocess.run(["sudo", "service", "lightdm", "start"])
    subprocess.run(["sudo","reboot","-f"])
else:
    print("PLEASE ENTER VALID INPUT \n")


