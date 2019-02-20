"""
    This module holds the class that makes
    subprocess calls to ffmpeg with the received
    CLI commands.
"""
import subprocess
import os


class Convertor:
    """
        Makes calls to subprocesses with arguments
        and commands received from the CLI.
    """

    def to_audio(self, _in, _out, bitrate='320k'):
        """
            Converts input file to audio format
        """
        _out = self.get_name_from_path(_out)
        commands = ['ffmpeg', '-i', '_in',
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
