"""
    This module holds the class that makes
    subprocess calls to ffmpeg with the received
    CLI commands.
"""
import subprocess
import os
import platform


class Convertor:
    """
        Makes calls to subprocesses with arguments
        and commands received from the CLI.
    """

    def to_audio(self, _in, _out, bitrate='320k'):
        """
            Converts input file to audio format
        """

        # Default output parameter
        if _out:
            _out += self.get_name_from_path(_in)
        commands = ['ffmpeg', '-i', _in,
                    '-vn', '-ar', '44100',
                    '-ac 2', '-ab',
                    bitrate, _out + '.mp3']
        subprocess.Popen(commands)

    def get_name_from_path(self, file_path):
        """
            Extracts file name from absolute file path.
        """

        head, tail = os.path.split(file_path)
        return tail or os.path.basename(head)

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

    def convert_multiple(self, video_files, out, brate):
        """
            Converts all files specified in directory.
        """

        for video in video_files:
            self.to_audio(video, out, brate)

    def load_player(self, playitems, preferred_player):
        """
            Opens up audio files in user audio player.
        """
        current_platform = platform.system()

        if preferred_player:
            try:
                self.openPlayer(preferred_player, playitems)
            except Exception as e:
                return f"Player {preferred_player} missing. "+
                "Try installing it"+
                " or use something different."
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
