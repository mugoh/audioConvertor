"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click
import os

from formats import Convertor


@click.group(invoke_without_command=True)
@click.option('--verbose', '-v', help="Increase output verbosity level")
@click.pass_context
def main(ctx, verbose):
    group_commands = ['convert', 'play']
    """
            audio3 is a command line tool that helps convert video files
            to audio file formats.\n
             example: audio3 convert -i input/file/path -o output/path
        """

    if ctx.invoked_subcommand is None:
        click.echo("Specify one of the commands below")
        print(*group_commands, sep='\n')


@main.command('convert')
@click.option('--input_directory', '-i', nargs=1, type=click.Path(exists=True),
              required=True, help="Directory to get files to convert")
@click.option('--output', '-o', nargs=1, type=click.Path(),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
@click.option('--bitrate', '-b', type=int,
              help="Audio bitrate specification in kbps e.g 192.\n" +
              "Default beatrate is 320k",
              default='320k')
@click.option('--recursive', '-r', is_flag=True,
              help="Load files from a directory")
@click.option('--file_format', '-f',
              help="Output format for files in mulitple conversion. " +
              "Specified with --recursive e.g mp3",
              default="mp3")
@click.pass_context
def load_files(ctx, input_directory, output, bitrate, recursive, file_format):
    """
        :   Convert video file input to audio.
    """
    if os.path.isfile(input_directory):
        click.echo("Output specified as file name")
        convertor_instance.to_audio(
            input_directory, output, bitrate, file_format)

    if recursive:
        try:
            os.listdir(input_directory)
            os.listdir(output)
            video_files = [[file_ for file_ in files
                            if convertor_instance.is_video(file_)]
                           for root, dirs, files
                           in os.walk(input_directory)]
        except NotADirectoryError as er:
            click.echo(input_directory, 'or', output,
                       " is a not a directory. " +
                       " Use --recursive with directories")
            click.echo(er)
        else:
            click.echo("Found ", video_files.length(), "files")
            click.echo(convertor_instance.show_process_message())
            convertor_instance.convert_multiple(video_files,
                                                output,
                                                bitrate,
                                                file_format
                                                )

        finally:
            pass


@main.command('play')
@click.option('playlist', '-p', required=True, type=click.Path(exists=True),
              help="Folder containing audio files to be played")
@click.option('--recursive', '-r', is_flag=True,
              help="Load files from a directory")
@click.option('--player', '-e',
              help="Preferred audio player to open audio files")
@click.pass_context
def load_audio(ctx, playlist, recursive, player):
    """
        :   Selects a track of audio files and loads them up
        in a music player.
    """
    if recursive:
        try:
            full_playlist = os.listdir(playlist)
        except FileNotFoundError as e:
            click.echo(playlist, "is not a directory")
        else:
            convertor_instance.load_player(
                full_playlist)
            pass
        finally:
            pass

    player_error = convertor_instance.load_player([playlist], player)

    if player_error:
        click.echo(player_error)


convertor_instance = Convertor()

if __name__ == '__main__':
    main()
