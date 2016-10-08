---
layout: post
title: "Simple audio setup"
date: 2016-9-30
extra_css: /css/post.css
---
*This post is mostly for my reference, as I forget half the things I do to my
laptop.*

Here are the tools that I use to manage simple audio:

* `pulseaudio`
* `alsa`
* `pavucontrol`
* `pulseaudio-ctl`
* `pasystray` 
* `xbindkeys`***

(In the case of `xbindkeys` I don't just use it for audio. This is useful to
map a combination of keys to run commands/scripts. I also use this to make lock
my computer and run xscreensaver.)

`pulseaudio` + `alsa` is the base audio configuration of the laptop, you can
run this to test if you're using this:
{% highlight bash %}
$ pactl list
$ aplay -l
{% endhighlight %}

### Main goal here:
Really, I can get away with just using `alsamixer`, although I don't really
want to go through a terminal everytime I want to mute the volume. My common
case (as is probably most people's) is to raise/lower volume. This is then
configured with keyboard shortcuts.

### HDMI audio redirect:
To control volume, input, or output devices a decent GUI interface to use is
`pavucontrol`'s. This allows you to redirect output stream from computer's
internal speakers to HDMI. This is a nice way of doing it, for when you're
connecting a projector to your laptop using HDMI.

### Keyboard shortcuts:
To increase or decrease volume with keyboard shortcuts I use `xbindkeys` +
`pulseaudio-ctl` commands. This is what worked for me in my `.xbindkeysrc` file
{% highlight bash %}
"/usr/bin/pulseaudio-ctl up"
	XF86AudioRaiseVolume

"/usr/bin/pulseaudio-ctl down"
	XF86AudioLowerVolume

"/usr/bin/pulseaudio-ctl mute"
	XF86AudioMute
{% endhighlight %}
then make sure to run `xbindkeys -p` to set keybindings.
[Here](https://wiki.archlinux.org/index.php/Xbindkeys) is a nice arch
linux wiki page.
To get the system tray icon, the AUR has `pasystray` package; this is coupled
with `stalonetray` in my case. This is definitely optional. I will probably
stop using it; although it's a nice visual indication of volume status.
