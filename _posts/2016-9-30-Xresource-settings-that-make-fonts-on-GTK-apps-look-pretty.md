---
layout: post
title: "Xresource settings that make fonts on GTK apps look pretty"
date: 2016-9-30
extra_css: /css/post.css
---
*This is a reference post for the setings on my computer*

I once found myself looking at menus with fonts that rendered horribly. Here I note
most of what I found to fix this on my laptop. The most important setting is
probs the anti-aliasing and hinting.

Figure out your own screen's dpi and replace it with the number below. The way I did
it is by using the `xorg-xdpyinfo` package and running `xdpyinfo | grep dots`.

The following goes into the `~/.Xresources` file. You also have to make sure
you run `xrdb -merge ~/.Xresources` for the changes to apply. I personally
have it in my `~/.xinitrc` file, but you do you.

{% highlight bash %}
! Xft settings
Xft.dpi:                    96
Xft.rgba:                   rgb
Xft.antialias:              true
Xft.hinting:                true
Xft.hintstyle:              hintslight
Xft.lcdfilter:              lcddefault
{% endhighlight %}
