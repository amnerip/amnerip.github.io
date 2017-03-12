---
layout: post
title: "USB Keyboard and Mouse suspends"
date: 2016-10-8
extra_css: /css/post.css
---

I bought a new mouse and keyboard recently. After rebooting my laptop, I found
that my mouse and keyboard had significant lag. A click or movement of the mouse
would take noticeable time for my laptop to
respond. After some googling, I found that my laptop was enabling power
management options for USB connected devices. This
[arch linux wiki page](https://wiki.archlinux.org/index.php/Power_management) is useful for more details.
Specifically, the
[tool](https://wiki.archlinux.org/index.php/Laptop_Mode_Tools) that I
have setup is Laptop Mode Tools. I wasn't aware of the default options for USB
devices, which was an autosuspend after 2 seconds:

{% highlight txt %}
# Set this to use opt-in/whitelist instead of opt-out/blacklist for deciding
# which devices should be autosuspended.
# AUTOSUSPEND_USE_WHITELIST=0 means AUTOSUSPEND_*_BLACKLIST will be used.
# AUTOSUSPEND_USE_WHITELIST=1 means AUTOSUSPEND_*_WHITELIST will be used.
AUTOSUSPEND_USE_WHITELIST=0

# The list of Device IDs that should not use autosuspend. Use system commands or
# look into sysfs to find out the IDs of your devices.
# Example: AUTOSUSPEND_DEVID_BLACKLIST="046d:c025 0123:abcd"
AUTOSUSPEND_RUNTIME_DEVID_BLACKLIST=""
...
# Auto-Suspend timeout in seconds
# Number of seconds after which the USB devices should suspend
AUTOSUSPEND_TIMEOUT=2
{% endhighlight %}

The above was found in the configuration file
`/etc/laptop-mode/conf.d/runtime-pm.conf`. My laptop for most of the time is
plugged into AC, so I switched to the opt-int whitelisting option. This
removed the issue that I was having with my
devices.

If you wanted to enable/disable this option, then typing `lsusb` would give you
the device ID that you would then have to add to the whitelist/blacklist.
