# xmastreething

A collection of simple scripts to manage/automate the [3D Xmas Tree for Raspberry Pi](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi). With these, it is possible to turn on/off the animated lights remotely. I did this so that it can be controlled from my [Lights](https://github.com/kenkl/lights) app, as a part of a scene/room.

### The scripts:

**checktree.py** - a simple True/False return of whether the tree's on right now. Not currently used for anything, but I have ideas...
**lighttree.py** - a wrapper script to check whether the tree is on, and turn it on (by launching xmastree.py) if it's not. I found that it was possible to launch multiple copies of the xmastree.py script. That makes treeoff.py unreliable - it expects a single PID to kill.
**xmastree.py** - the main animation script.
**treeoff.py** - a script that will stop the xmastree.py script, turning off all the LEDs.
**treecontroller.py** - a simple Flask application to listen for HTTP calls to turn the tree on or off. 

### Prerequisites

These scripts were developed on a Raspbian 10 (Buster) Lite installation. Python3 is present by default, but we also need PIP, which is easy enough to install:

```
sudo apt-get update
sudo apt-get install python3-pip
```

Once PIP is installed, we'll also need GPIOZERO, Flask, and all their dependencies. I've included a requirements.txt (using [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/) which should make installing everything a pretty straightforward operation:

```
sudo pip3 install -r requirements.txt
```

For more information on PIP, [RTFM](https://pip.pypa.io/en/stable/).

### Installation

I used the default 'pi' user's home directory, /home/pi, to house these scripts in the 'xmastreething' directory. Then, I added a couple lines to /etc/rc.local to launch the tree lights and treecontroller scripts:

```
su -c 'cd /home/pi/xmastreething && /home/pi/xmastreething/lighttree.py &' pi 
su -c 'cd /home/pi/xmastreething && /home/pi/xmastreething/treecontroller.py &' pi 
```

As shown, they do run as the 'pi' user; adjust for your situation as necessary.

### Use

Once launched, the animation will run continuously as long as the RPi is running (or it crashes or whatever). On my network, I've named it xmastree2 and it's known by my DNS server, so it's simple enough to control:

[http://xmastree2.kenkl.org:5000/treeon](http://xmastree2.kenkl.org:5000/treeon) - turns the tree on. If it's already on, no action will be taken.
[http://xmastree2.kenkl.org:5000/treeoff](http://xmastree2.kenkl.org:5000/treeoff) - turns it off. If it's already off, nothing notable happens. If you're watching flask output, you will see kill fail when it can't find the PID.

Note: xmastree2.kenkl.org is not accessible outside my network (of course); those links won't do anything if you click on 'em.

### The future

There is a new version of the hardware available: [3D RGB Xmas Tree](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi) for Raspberry Pi. They do have a [GitHub](https://github.com/ThePiHut/rgbxmastree) for the code that drives it. I've a couple copies in transit, and plan to fold the new code into this project once they arrive. I'm on the other side of the pond, in the US, and it seems unlikely that they'll arrive before Xmas. Watch this space, I guess.

I do see some fun things going on in the new version  - tree.off() would eliminate the Popen tomfoolery I'm doing here - I may try to adapt the new code to the old tree. 





