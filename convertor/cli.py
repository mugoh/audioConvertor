"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click
import os


@click.group()
@click.option('--input_directory', '-i', nargs=1, type=click.Path(exists=True),
              required=True, help="Directory to get files to convert")
@click.option('--output', '-o', nargs=1, type=click.Path(exists=True),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
@click.option('--bitrate', '-b', type=int,
              help="Audio bitrate specification in kbps e.g 192")
@click.option('--verbose', '-v', help="Increase output verbosity level")
@click.pass_context
def main(ctx, input_directory, output, bitrate, verbose):
    """
        audio3 is a command line tool that helps convert video files
        to audio file formats.\n
         example: audio3 convert -i input/file/path -o output/path
    """
    ctx.obj = input_directory
    ctx.obj = output


"""@main.command('convert')
@click.option('--input_directory', '-i', nargs=1, type=click.Path(exists=True),
              required=True, help="Directory to get files to convert")
@click.option('--output', '-o', nargs=1, type=click.Path(exists=True),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
@click.option('--bitrate', '-b', type=int,
              help="Audio bitrate specification in kbps e.g 192")
@click.pass_obj
"""


@main.command('convert')
@click.pass_context
def load_files(ctx):
    """
        :   Convert video file input to audio.
    """
    output = ctx.obj
    for file in os.listdir(output):
        click.echo(file)


@main.command('play')
@click.option('playlist', '-p', required=True, type=click.Path(exists=True),
              help="Folder containing audio files to be played")
@click.pass_context
def load_audio(ctx, playlist):
    """
        :   Selects a track of audio files and loads them up
        in a music player.
    """
    playlist = os.listdir(playlist)


if __name__ == '__main__':
    main()
