"""
    This module holds functions that help in
    type checking and of the application arguments
    and function parameters.
"""
import click
import subprocess


def check_is_video(file_name):
    """
        Ensures passed file inputs are of recogninsed
        media format.
    """
    formats = ['flv', 'mp4', 'avi']

    return any([extension for extension in
                formats if file_name.endswith(extension)])


@click.command()
@click.option('--choice_', type=click.Choice(['y', 'n'],
                                             case_sensitive=False))
def require_ffmepg():
    """
        Prompts for installation of ffmpeg from user
        if missing. If user specifies 'No', the
        convertion is terminated.
    """
    choices = ['y', 'n']

    choice_ = input("Need to get ffmpeg. Continue?[y/n] ").lower().strip()[0]
    click.echo("choice " + choice_)

    while choice_ not in choices:
        choice_ = input("Continue? y/n ").lower().strip()[0]
    if choice_ == 'n':
        return
    elif choice_ == 'y':
        get_module('ffmpeg')


def get_module(module):
    """
        Fetches and installs dependency that matches
        given parameter name.
    """

    subprocess.Popen(['pip', 'install', module])
