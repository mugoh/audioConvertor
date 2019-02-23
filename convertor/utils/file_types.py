"""
    This module holds functions that help in
    type checking and of the application arguments
    and function parameters.
"""
import click


def check_is_video(file_name):
    """
        Ensures passed file inputs are of recogninsed
        media format.
    """
    formats = ['flv', 'mp4', 'avi']

    return any([extension for extension in
                formats if file_name.endswith(extension)])


@click.argument('--choice_', choices=['y', 'n'],
                prompt="Need to get ffmpeg. Continue? [y/N]")
def require_ffmepg(choice_):
    """
        Prompts for installation of ffmpeg from user
        if missing. If user specifies 'No', the
        convertion is terminated.
    """
    click.echo("choice " + choice_)
