"""Tests for `utm_epsg_finder`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import utm_epsg_finder
from utm_epsg_finder import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "utm_epsg_finder.cli.main"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { utm_epsg_finder.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
