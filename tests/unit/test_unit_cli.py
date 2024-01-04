"""CLI test."""
import unittest

from click.testing import CliRunner

from talisman.cli import main
from tests import OUTPUT_DIR

CLI_OUTPUT_DIR = OUTPUT_DIR / "cli"


class TestCommandLineInterface(unittest.TestCase):
    """Tests all command-line subcommands."""

    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
        self.runner = runner

    def test_main_help(self):
        result = self.runner.invoke(main, ["--help"])
        out = result.stdout
        self.assertIn("extract", out)
        self.assertIn("halo", out)
        self.assertEqual(0, result.exit_code)
