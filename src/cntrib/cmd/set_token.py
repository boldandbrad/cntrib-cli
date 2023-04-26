import click

from cntrib.util.token_util import set_gh_token


@click.command(name="set-token")
@click.argument("token")
@click.help_option("-h", "--help")
def set_token(token) -> None:
    """Store GitHub token.

    - TOKEN is the GitHub token to store.
    """
    set_gh_token(token)
    print("GitHub token set.")
