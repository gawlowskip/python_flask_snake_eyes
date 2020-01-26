import subprocess

import click


@click.command()
@click.option('--name', default='', help='Your name')
@click.argument('argname', default='')
def cli(name, argname):
    """
    Run hello to invite a new friend

    :param name: Your name
    :param argname: Your name
    :return: Return Hi and your name
    """

    if argname:
        click.echo(f"Hi {argname}")
        return

    click.echo(f"Hi {name}")

