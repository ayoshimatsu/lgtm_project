import click

@click.command()
@click.option("--message", "-m", default="LGTM", show_default=True, help="Characters on picture")
@click.argument("keyword")
def cli(keyword, message):
    """LGTM tool"""
    lgtm(keyword, message)
    click.echo("lgtm")

def lgtm(keyword, message):
    pass


