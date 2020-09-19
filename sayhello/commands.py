import click

from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

@app.shell_context_processor
def shell_context():
    return dict(db=db,Message=Message)

# @app.cli.command()
# @click.option('--count',default=20,help='Quantity of messages, default is 20.')
# def forge(count):

