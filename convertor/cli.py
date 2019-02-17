"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click
import os


@click.command(context_settings={
    "ignore_unknown_options": True
})
@click.argument('Input', nargs=-1, type=click.Path(exists=True),
                required=True)
@click.option('--output', '-o', nargs=1, type=click.Path(exists=True),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
def load_files(Input, output):
    """
        INPUT: Path to file(s) to convert\n
    """
    for file in os.listdir(output):
        click.echo(file)


if __name__ == '__main__':
    load_files()
