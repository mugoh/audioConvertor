"""
    This module holds the presentation of the application's
    functionality to the user on a command line.
"""

import click
import os

from formats import Convertor


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--verbose', '-v', help="Increase output verbosity level")
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
    ctx.obj['VERBOSE'] = True


@main.command('convert')
@click.pass_context
@click.option('--input_directory', '-i', multiple=True,
              type=click.Path(exists=True),
              required=True, help="Directory to get files to convert")
@click.option('--output', '-o', nargs=1, type=click.Path(exists=True),
              help="Path to save converted file.\n" +
              "Defaults to the current working directory if not specified",
              default='.')
@click.option('--bitrate', '-b',
              help="Audio bitrate specification in kbps e.g 192.\n" +
              "Default beatrate is 320k",
              default='320k')
@click.option('--recursive', '-r', is_flag=True,
              help="Load files from a directory")
@click.option('--file_format', '-f',
              help="Output format for files in multiple conversion. " +
              "Specified with --recursive e.g mp3",
              default="mp3")
def load_files(ctx, input_directory, output, bitrate, recursive, file_format):
    """
        :   Convert video file input to audio.
    """
    user_input = convertor_instance.split_input_dirs(input_directory)
    for path in user_input:
        input_directory = path

        if os.path.isfile(input_directory) and not recursive:
            click.echo("Input specified as file name")
            convertor_instance.to_audio(
                input_directory, output, bitrate, file_format)
        if not recursive and os.path.isdir(input_directory):
            click.echo(
                input_directory +
                " is a directory. " + "--recursive Needed for directory")

        if recursive:
            try:
                os.listdir(input_directory)
                os.listdir(output)

                # for root, dirs, files in os.walk(input_directory):
                #    click.echo(files)
                # print([
                # files for root, dirs, files in os.walk(input_directory)
                # if])

                nested_files = [os.path.join(root, file_)
                                for root, dirs, files
                                in os.walk(input_directory)
                                for file_ in files]

                video_files = [file_ for file_ in flatten(nested_files)
                               if convertor_instance.is_video(file_)]
                if not video_files:
                    click.echo("\nCould not find video format files in " +
                               input_directory,
                               err=True)
                    return

            except NotADirectoryError as er:
                click.echo(input_directory + ' or ' + output +
                           " is a not a directory. " +
                           " Use --recursive with directories")
                click.echo(er, err=True)
            else:
                click.echo("Found " + str(len(video_files)) + " files")
                click.echo(click.style(
                    convertor_instance.show_process_message(), blink=True,
                    fg='yellow', bold=True))
                convertor_instance.convert_multiple(video_files,
                                                    output,
                                                    bitrate,
                                                    file_format
                                                    )

            finally:
                return


@main.command('play')
@click.pass_context
@click.option('playlist', '-p', required=True, type=click.Path(exists=True),
              help="Folder containing audio files to be played")
@click.option('--recursive', '-r', is_flag=True,
              help="Load files from a directory")
@click.option('--player', '-pl',
              help="Preferred audio player to open audio files")
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
            return

    if not convertor_instance.is_video(playlist):
        click.echo(click.style(
            playlist + " is not a supported media type", fg='red'))
    player_error = convertor_instance.load_player([playlist], player)

    if player_error:
        click.echo(player_error, err=True)


def flatten(iterable):
    """
      Extracts nested file items from path
      to single iter.
    """
    return iterable

    # Os walk with absolute path returns
    # non-nested
    #
    # return [item for it in iterable for item in it]


convertor_instance = Convertor()

if __name__ == '__main__':
    main(obj={})
