#!/usr/bin/env python
import click
import sys


def marco(name):
    if name == "Marco":
        return "Polo"
    return "No!"


@click.command()
@click.option('--name')
def callmarco(name):
    result = marco(name)
    if result != "Marco":
        click.echo(click.style(f'{result}', bg='red'))
        sys.exit(0)
    click.echo(result)
    #click.echo(click.style(f'{result}', bg='green')) 

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callmarco()