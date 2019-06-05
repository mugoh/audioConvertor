"""
    This module holds the class that makes
    subprocess calls to ffmpeg with the received
    CLI commands.
"""
import subprocess
import os
import platform
from click import echo, style

from utils.file_types import require_ffmepg, check_is_video


class Convertor:
    """
        Makes calls to subprocesses with arguments
        and commands received from the CLI.
    """

    def to_audio(self, _in, _out, bitrate, file_format):
        """
            Converts input file to audio format
        """

        # Default output parameter
        # If not current directory, append '/'
        if os.path.isdir(_out):
            _out = '' if _out == '.' else _out + '/'
            _out += self.get_name_from_path(_in,
                                            replace=True) + '.' + file_format

        # File format unchecked for single inputs
        if not check_is_video(_in):
            msg = " is not a supported media type"
            self.abort_conversion(
                self.get_name_from_path(_in) + msg)

        """
        else:
            base_name = os.path.basename(_out)
            ext = os.path.splitext(base_name)[1]
            _out = _out.replace(ext, '.mp3')
        """
        commands = ['ffmpeg', '-i', _in,
                    '-vn', '-ar', '44100',
                    '-ac', '2', '-ab',
                    bitrate, _out]
        try:
            self.run_convert_commands(commands)
        except FileNotFoundError as er:
            res = require_ffmepg()

            if not res:
                self.abort_conversion("Dependecy not installed.")

    def get_name_from_path(self, file_path, replace=False):
        """
            Extracts file name from absolute file path.
        """

        if replace:
            base_name = os.path.basename(file_path)
            ext = os.path.splitext(base_name)[1]
            _out = base_name.replace(ext, '')
            return _out

        head, tail = os.path.split(file_path)
        return tail or os.path.basename(head)

    def run_convert_commands(self, cmds):
        """
            Invokes subprocess with commands
            required to process a user input call.
        """
        try:
            subprocess.check_output(cmds)
        except subprocess.CalledProcessError as er:
            print("Unable to complete conversion\n", er)
        else:
            echo(style("\nConversion Complete\n", fg='green'))
            echo("Saved: " + cmds[len(cmds) - 1])

    def is_video(self, given_file):
        """
            Checks if given file has a video format based on the
            file extension.
        """
        video_extensions = ['mp4', 'flv', 'avi', 'mp3', 'flaac']

        return any([ext for ext in video_extensions
                    if given_file.endswith(ext)])

    def show_process_message(self):
        """
            Displays conversion process start to the user.
        """

        return "Converting"

    def convert_multiple(self, video_files, out, brate, _format):
        """
            Converts all files specified in directory.
        """

        for video in video_files:
            self.to_audio(os.path.abspath(video),
                          out, brate, _format)

    def load_player(self, playitems, preferred_player):
        """
            Opens up audio files in user audio player.
        """
        error = False

        current_platform = platform.system()

        if preferred_player:
            try:
                open_status = self.open_player(preferred_player, playitems)

                if not open_status:
                    error = True
                    return error
            except Exception as e:
                msg = f'Player {preferred_player} missing. '
                echo(msg + "Try installing it" +
                     " or use something different.")
                error = True
            else:
                pass
            finally:
                return error

        if current_platform == 'Linux':
            self.open_player('xdg-open', playitems)
        elif current_platform == 'Darwin':
            self.open_player('open', playitems)
        elif current_platform == 'Windows':
            self.open_player(play_items=playitems)

    def open_player(self, cmd=[], play_items=[]):
        """
            Opens user audio player depending on present
            system architecture.
        """
        commands = [cmd] + play_items

        try:
            subprocess.check_call(commands)
        except subprocess.CalledProcessError as er:
            return False
        else:
            return True

    def abort_conversion(self, message=''):
        """
            Terminates app process with message.
        """
        exit_message = ' Aborted'
        message += exit_message
        echo(style('\n' + message, fg='red'))

        os.abort()

    def split_input_dirs(self, paths):
        """
            Gives individual input paths from
            a tuple of input paths
        """

        for path in paths:
            yield path
