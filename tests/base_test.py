"""
    This module holds the base test class
"""
from click.testing import CliRunner
import os

from convertor.cli import main


class BaseTestCase():
    """
        Creates dummy data and methods for aiding the
        app's testing
    """

    def setUp(self):
        """
            Initializes test data
        """
        self.runner = CliRunner()

        try:
            self.input_f = os.mkdir('dummy_t')
        except FileExistsError:
            self.input_f = os.path.abspath('dummy_t')

    def invoke(self, cmds=[], inputs=[]):
        """
            Invokes commands to Runner
        """
        inputs = '\n'.join(inputs)
        return self.runner.invoke(main, args=cmds, input=inputs)
