"""
    This module holds the class that makes
    subprocess calls to ffmpeg with the received
    CLI commands.
"""
import subprocess
import os
import platform
from click import echo

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
            echo("\nConversion Complete")
            echo("Saved: " + cmds[len(cmds) - 1])

    def is_video(self, given_file):
        """
            Checks if given file has a video format based on the
            file extension.
        """
        video_extensions = ['mp4', 'flv', 'avi']

        return any([ext for ext in video_extensions
                    if given_file.endswith(ext)])

    def show_process_message(self):
        """
            Displays convertertion process start to the user.
        """

        return "Converting"

    def convert_multiple(self, video_files, out, brate, _format):
        """
            Converts all files specified in directory.
        """

        for video in video_files:
            self.to_audio(video, out, brate, _format)

    def load_player(self, playitems, preferred_player):
        """
            Opens up audio files in user audio player.
        """
        current_platform = platform.system()

        if preferred_player:
            try:
                self.openPlayer(preferred_player, playitems)
            except Exception as e:
                msg = f'Player {preferred_player} missing. '
                return msg
                + "Try installing it"
                + " or use something different."

            else:
                pass
            finally:
                pass

        if current_platform == 'Linux':
            self.openPlayer('xdg-open', playitems)
        elif current_platform == 'Darwin':
            self.openPlayer('open', playitems)
        elif current_platform == 'Windows':
            self.openPlayer('', playitems)

    def open_player(self, cmd, play_items):
        """
            Opens user auio player epending on present
            system architecture.
        """
        commands = [cmd]
        subprocess.Popen(commands + play_items,
                         shell=True)

    def abort_conversion(self, message=''):
        """
            Terminates app process with message.
        """
        exit_message = ' Aborted'
        message += exit_message
        echo('\n', message)

        os.abort()
