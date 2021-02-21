"""Console script for utm-epsg-finder."""
import click

from utm_epsg_finder import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> int:
    """Console script for utm-epsg-finder."""
    click.echo("Replace this message by putting your code into utm_epsg_finder.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
