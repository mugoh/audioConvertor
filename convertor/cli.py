"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click


@click.command(context_settings={
    "ignore_unknown_options": True
})
@click.argument('input_files', nargs=-1,
                type=click.Path(exists=True),
                help="The path to file(s) to convert")
def load_files(input_files):
    for file in input_files:
        click.echo(file)


if __name__ == '__main__':
    load_files()
