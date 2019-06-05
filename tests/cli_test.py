"""
    This module holds tests for the applications'
    interface
"""

from .base_test import BaseTestCase


class TestCLI(BaseTestCase):

    def test_run_without_subcommands(self):
        self.setUp()
        res = self.invoke()

        print(res.output)
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

    def test_convert_multiple_files_no_media(self):
        self.setUp()

        res = self.invoke(
            cmds=[
                'convert',
                '--input_directory',
                'convertor/' + '',
                '--recursive'],
            inputs=[
                self.input_f])

        print(res.output)
        assert res.exit_code == 0
        assert 'Could not find' in res.output
