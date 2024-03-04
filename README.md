# Fix-Linux-BlackScreen

Most Linux users face the black screen issue after installing 
the operating system and trying to log in.

So I designed this simple script to solve this problem by executing some Linux commands automatically.
All you have to do is download the tool, run it, and then choose the type of display manager that you installed during the system installation.

`If you want to change it, just choose the corresponding option`

## Steps

1- Press `Ctrl`+`Alt`+`f2`or `f3` 

2- Login 
 
3- Run these commands
 ```bash 
 git clone https://github.com/V3ENIOM/Fix-Linux-Black-Screen.git
 ```
    cd Fix-Linux-BlackScreen
 ```
 sudo python3 Script.py
 ````

If this window appears, choose your preferred interface

![](https://i.ibb.co/v45YsFv/Virtual-Box-Kali-04-03-2024-17-38-18.png)

<hr/>

**IF Login Page Appeared and is still refreshing. Switch to Previous session using `Ctrl`+`Alt`+`f2`or `f3` 
and Wait for the download to complete**
<hr/>

**If the Script doesn't Work Correctly, run these commands...**

 ```bash
    sudo apt auto-remove
```
```
    sudo reboot -f 
```
