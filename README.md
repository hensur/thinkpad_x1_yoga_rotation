# Automatic tablet mode on Thinkpad Yoga 370

The Thinkpad Yoga 370 is a convertible laptop, so you can flip the screen over and your laptop is now a tablet.
Gnome can detect a screen rotation in recent versions and will rotate the screen automatically.
I had to install [iio-sensor-proxy](https://github.com/hadess/iio-sensor-proxy) to have working screen rotation. It can optionally be enabled in the script if you use another DE (see [installation](#installation)).

However, this leaves the touchpad and trackpoint enabled. This tool will detect if the Yoga is in Tablet mode and disable these devices.
It will also disable the Wacom Finger Touch if the pen is near the screen.

I've tested it on ArchLinux with kernel 4.14.13-1-ARCH. It should work on other distros as well.

## prerequisites
* linux packages: `xorg-xrandr acpid python-dbus iio-sensor-proxy python-docopt xorg-xinput xf86-input-wacom python`

## installation

If you are an Archlinux User install the AUR Package: [yoga370d-git](https://aur.archlinux.org/packages/yoga370d-git/)

Else just clone the repo and execute the script as your user. If you copy it to /usr/local/bin/yoga370d it can be used with the supplied .desktop file.

## usage

This python script provides the following features:

* Listen to dbus signals from sensor proxy and detect when the laptop is converted to tablet mode. Then touchpad and trackpoint are switched off. When going back to laptop mode the orginal state is restored.
* disable finger touch if stylus is close to the display
* upon termination, switch on touchpad and trackpoint
* Change `ROTATE_ACTIVE = False` in the top of the script to `ROTATE_ACTIVE = True` to enable screen rotation as well if your DE does not support it.

```
./yoga370d
```

### setup autostart

In recent versions Gnome won't allow you to put commands into autostart anymore. To enable it you have to put the .desktop file from the repo into `~/.config/autostart/`.
Or, if you used my PKGBUILD, you can just copy it there:
```
cp /usr/share/applications/yoga370d.desktop ~/.config/autostart/
```

## References/Kudos

* https://github.com/sarmbruster/thinkpad_x1_yoga_rotation
* https://classicforum.manjaro.org/index.php?topic=9671.0
* https://github.com/wdbm/spin
