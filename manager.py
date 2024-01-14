#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from datetime import date, datetime
import glob
import subprocess
import sys
import os
from subprocess import call

"""
The central hub for all things about developing this site.
- Create a new post.
- Start/Stop server. [TODO]
"""
EDITOR = os.environ.get('EDITOR', 'vim')
DEFAULT_POST_TITLE = "new-post"
DEFAULT_DATE = date.today()
POSTS_LOC = "_posts"
MD_POSTS_HEADER = """\
---
layout: post
title: "{spaces_title}"
date: {year}-{month}-{day}
extra_css: /css/post.css
---
"""
LOG = "localhost-output.log"
KILL_MESSAGE = f"""\
Server started. Run './manager.py --stop-server' to stop it. {LOG} for server logs."""

def setup_args():
    parser = argparse.ArgumentParser(
        "Development environment for blog; automates various actions")
    parser.set_defaults(func=main)

    subparsers = parser.add_subparsers(
        help="different actions you can work on.")

    # General settings
    server_group = parser.add_mutually_exclusive_group()
    server_group.add_argument(
        "-r",
        dest="start",
        action="store_true",
        help="Start the jekyll server"
    )

    server_group.add_argument(
        "-k",
        dest="stop",
        action="store_true",
        help="Stop jekyll server"
    )

    # Manage blog posts
    post_parser = subparsers.add_parser(
        "posts",
        help="Create or edit a post"
    )
    post_parser.set_defaults(func=posts)
    actions = post_parser.add_mutually_exclusive_group()
    actions.add_argument(
        "--create",
        action="store_true",
        help="Make a new post, and edit it in the local $EDITOR"
    )
    actions.add_argument(
        "--edit",
        action="store_true",
        help="Pass in a value to --title, and $EDITOR will open it up."
    )

    post_parser.add_argument(
        "--date",
        action="store",
        default=DEFAULT_DATE,
        type=parse_date,
        help="Set a date for the post. Default is today. Required format: "
             "YYYY-MM-DD"
    )
    post_parser.add_argument(
        "--title",
        action="store",
        required=True,
        default=DEFAULT_POST_TITLE,
        help="Title of associated post."
    )
    
    return parser


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def posts(args):
    posts_loc = POSTS_LOC
    # Generate the filename:
    post_date = args.date
    year, month, day = post_date.year, post_date.month, post_date.day
    title = args.title.split()
    spaces_title = " ".join(title)
    header = MD_POSTS_HEADER.format(**locals())
    dash_title="-".join(title)
    
    filename = \
        "{posts_loc}/{year}-{month}-{day}-{dash_title}.md"\
        .format(**locals())

    # Open and edit the new post
    if args.create:
        print("Created file {}".format(filename))
        with open(filename, 'w') as f:
            f.write(header)
            f.flush()
            call([EDITOR, filename])
    elif args.edit:
        posts_paths = glob.glob("{posts_loc}/*.md".format(**locals()))
        post_files = [post.split("/")[-1] for post in posts_paths]
        strip_sfx = [post.split(".")[0] for post in post_files]

        # Map path to post title
        titles_to_paths = {}
        for i, post in enumerate(strip_sfx):
            post_title = post.split("-")[3:]
            path = posts_paths[i]
            titles_to_paths[" ".join(post_title)] = path

        path = titles_to_paths[args.title]
        print("Editing post {path}".format(**locals()))
        call([EDITOR, path])
    elif args.title:
        # TODO: print information about the post
        pass

def main(args):
    if args.start:
        find_jekyll = "pkill -0 -f jekyll"
        ret = subprocess.call(find_jekyll.split())
        if ret == 0:
            print("Server is already running.")
        else:
            subprocess.Popen(
                "jekyll serve &".split(),
                stderr=subprocess.STDOUT,
                stdout=open(LOG, 'w'))
            print(KILL_MESSAGE)
    elif args.stop:
        ret = subprocess.call("pkill -f jekyll".split())
        if ret == 0:
            print("Server killed.")
        else:
            print("Nothing was found to stop")
    pass

if __name__ == '__main__':
    args = setup_args().parse_args()
    args.func(args)
