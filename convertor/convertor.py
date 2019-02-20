"""
    This module holds the class that makes
    subprocess calls to ffmeg with the received
    CLI commands.
"""
import subprocess
import shutil


class Convertor:
    """
        Makes calls to subprocesses with arguments
        and commands received from the CLI.
    """
    def __init__():
        """
            Checks for presence of ffmpeg on program start
            in urs/bin and prompts for installation.
        """

        if not shutil.which('ffmpeg'):
            install_prompt = input(
                "Need to get ffmpeg for you. Continue?[y/N] ")
            accepted_res = ['y',  'n']
            while install_prompt.lower()[0] not in accepted_res:
                install_prompt = input()
