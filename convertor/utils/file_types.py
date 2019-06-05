"""
    This module holds functions that help in
    type checking and of the application arguments
    and function parameters.
"""
import click
import subprocess


def check_is_video(file_name):
    """
        Ensures passed file inputs are of recognized
        media format.
    """
    formats = ['flv', 'mp4', 'avi', 'mp3', 'flaac']

    return any([extension for extension in
                formats if file_name.endswith(extension)])


def require_ffmepg():
    """
        Prompts for installation of ffmpeg from user
        if missing. If user specifies 'No', the
        conversion is terminated.
    """
    choices = ['y', 'n']

    choice_ = input("Need to get ffmpeg. Continue?[y/n] ").lower().strip()[0]

    while choice_ not in choices:
        choice_ = input("Continue? y/n ").lower().strip()[0]
    if choice_ == 'n':
        return False
    elif choice_ == 'y':
        get_module('ffmpeg')
        return True


def get_module(module):
    """
        Fetches and installs dependency that matches
        given parameter name.
    """

    click.echo("\nGetting ffmpeg")

    try:
        subprocess.check_call(['sudo', 'apt-get', 'install', module])
    except subprocess.CalledProcessError as e:
        print("Could not get ", module, '\n', e)
