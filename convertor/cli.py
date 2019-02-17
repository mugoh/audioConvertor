"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click
import os


@click.group()
@click.pass_context
@click.option('--verbose', '-v', help="Increase output verbosity level")
def main(ctx):
    """
        audio3 is a command line tool that helps convert video files
        to audio file formats.\n
         example: audio3 convert -i input/file/path -o output/path
    """
    pass


@main.command('convert')
@click.option('--input_directory', '-i', nargs=1, type=click.Path(exists=True),
              required=True, help="Directory to get files to convert")
@click.option('--output', '-o', nargs=1, type=click.Path(exists=True),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
@click.pass_obj
def load_files(ctx, input_directory, output):
    """
        :   Convert video file input to audio.
    """
    for file in os.listdir(output):
        click.echo(file)


if __name__ == '__main__':
    main()
