"""
    This module holds tests for the applications'
    interface
"""

from .base_test import BaseTestCase

import os


class TestCLI(BaseTestCase):

    def test_run_without_subcommands(self):
        self.setUp()
        res = self.invoke()

        assert 'Specify one' in res.output
        assert res.exit_code == 0

    def test_convert_single_file_no_media(self):
        self.setUp()

        res = self.invoke(
            cmds=['convert', '--input_directory', self.input_f, '--recursive'],
            inputs=[self.input_f])

        assert res.exit_code == 0
        assert 'Could not find' in res.output

    def test_convert_single_file_no_recursive(self):
        self.setUp()

        res = self.invoke(
            cmds=['convert', '--input_directory', self.input_f],
            inputs=[self.input_f])

        assert res.exit_code == 0
        assert 'recursive Needed' in res.output

    def test_convert_missing_file(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'convert',
                '--input_directory',
                'convertor/examples/media/sno*' + '',
                ''],
            inputs=[
                self.input_f])

        assert res.exit_code == 2
        assert 'not exist' in res.output

    def test_convert_file(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'convert',
                '--input_directory',
                'convertor/examples/media/snoring_noises.mp3' + ''],
            inputs=[
                self.input_f])

        assert res.exit_code == 0
        assert 'Complete' in res.output
        self.clear()

    def test_convert_files_recursively(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'convert',
                '--input_directory',
                'convertor/examples/media/' + '',
                '--recursive'],
            inputs=[
                self.input_f])

        assert res.exit_code == 0
        assert 'Complete' in res.output
        self.clear()

    def clear(self):
        """
            Removes saved file
        """
        try:
            os.remove('snoring_noises.mp3')
        except FileNotFoundError:
            pass

    def test_play_media_without_recursive_specified(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'play',
                '--playlist',
                'convertor/examples/media/' + '',
            ],
            inputs=[
                self.input_f])

        assert res.exit_code == 0
        assert 'not a supported media' in res.output

    def test_play_single_media_with_recursive(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'play',
                '--playlist',
                'convertor/examples/media/snoring_noises.mp3' + '',
                '--recursive'],
            inputs=[
                self.input_f])

        assert res.exit_code == 0
        assert 'not a directory' in res.output

    def test_play_multiple_media_as_recursive(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'play',
                '--playlist',
                './convertor/examples/media/',
                '--recursive'], inputs=[
                self.input_f])
        assert res.exit_code == 0

    def test_play_media(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'play',
                '--playlist',
                'convertor/examples/media/snoring_noises.mp3' + '',
            ])

        assert res.exit_code == 0
