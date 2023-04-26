import click

from cntrib.cmd import clear_token, set_token
from cntrib.util.cmd_util import SectionedHelpGroup

commands = {
    "Contribution Commands": [],
    "Other Commands": [
        clear_token,
        set_token,
    ],
}


@click.group(
    cls=SectionedHelpGroup,
    help="Check your GitHub contributions in your terminal.",
)
@click.help_option("-h", "--help")
@click.version_option(
    None,  # use version auto discovery
    "-v",
    "--version",
    package_name="cntrib-cli",
    message="%(prog)s-cli, v%(version)s",
)
def cli() -> None:
    """Main 'cntrib' command."""
    pass


for section, cmds in commands.items():
    for cmd in cmds:
        cli.add_command(cmd, section=section)

if __name__ == "__main__":
    cli()
