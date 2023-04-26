import click

from cntrib.util.token_util import clear_gh_token


@click.command(name="clear-token")
@click.help_option("-h", "--help")
def clear_token() -> None:
    """Clear GitHub token."""
    clear_gh_token()
    print("GitHub token cleared.")
