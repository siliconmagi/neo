import click


@click.command()
@click.option('--string', default='Plane',
              help='Concat this')
@click.option('--repeat', default=1,
              help='Repeat this many times')
def done(string, repeat):
    """Done App"""
    for x in range(repeat):
        click.echo('Hello %s!' % string)
