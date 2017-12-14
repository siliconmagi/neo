import click


@click.command()
@click.option('--string', default='Plane',
              help='Concat this')
@click.option('--repeat', default=1,
              help='Repeat this many times')
@click.argument('out', type=click.File('W'))
def done(string, repeat, out):
    """Done App"""
    click.echo(out)
    for x in range(repeat):
        click.echo('Hello %s!' % string)
e
