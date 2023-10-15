# Implementing the CLI feature
# Help Info
# Bind arguments to functions from user commands from the terminal
import os
import typer
from time import sleep
from rich.console import Console
from rich.table import Table

from core.models import Base
from core.config import engine
from core.passman import read_all, insert_pass, search, delete

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

console = Console()

app = typer.Typer()


@app.command(short_help='Adds a managed account')
def add(account: str, password: str):
    typer.echo(f"Saving password for your {account} account...")
    insert_pass(account.lower(), password)
    show()

@app.command(short_help='Delete one managed account')
def delete(account: str):
    typer.echo(f"Deleting this account -> {account}...")
    delete(account)
    show()

# @app.command()
# def update(position: int, task: str = None, category: str = None):
#     typer.echo(f"updating {position}")
#     update_todo(position-1, task, category)
#     show()


@app.command(short_help='shows all managed passwords')
def show():
    hashes = read_all()

    console.print("[bold magenta]CLI Password Manager![/bold magenta]!=", "💻")

    typer.echo(f"Querying for all accounts...")
    sleep(1)

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("UUID", min_width=20)
    table.add_column("ACCOUNT", min_width=12, justify="right")
    # table.add_column("PASSWORD", min_width=12, justify="right")
    table.add_column("DATE_CREATED", min_width=12, justify="right")

    # def get_category_color(category):
    #     COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
    #     if category in COLORS:
    #         return COLORS[category]
    #     return 'white'

    for index, hash in enumerate(hashes, start=1):
        # c = get_category_color(task.category)
        # is_done_str = '✅' if task.status == 2 else '❌'
        # table.add_row(str(index), hash.task, f'[{c}]{task.category}[/{c}]', is_done_str)
        # table.add_row(str(index), hash.unique_id, hash.account, hash.password, hash.date_created.strftime("%H:%M %B %d, %Y"))
        table.add_row(str(index), hash.unique_id, hash.account,
                      hash.date_created.strftime("%H:%M %B %d, %Y"))

    console.print(table)


@app.command(short_help='shows account password')
def account(account: str):
    hashes = search(account.lower())

    console.print("[bold magenta]CLI Password Manager![/bold magenta]!=", "💻")

    typer.echo(f"Searching password for this account -> {account}...")
    sleep(1)

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("UUID", min_width=20)
    table.add_column("ACCOUNT", min_width=12, justify="right")
    table.add_column("PASSWORD", min_width=12, justify="right")
    table.add_column("DATE_CREATED", min_width=12, justify="right")

    # def get_category_color(category):
    #     COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
    #     if category in COLORS:
    #         return COLORS[category]
    #     return 'white'

    for index, hash in enumerate(hashes, start=1):
        # c = get_category_color(task.category)
        # is_done_str = '✅' if task.status == 2 else '❌'
        # table.add_row(str(index), hash.task, f'[{c}]{task.category}[/{c}]', is_done_str)
        # table.add_row(str(index), hash.unique_id, hash.account, hash.password, hash.date_created.strftime("%H:%M %B %d, %Y"))
        table.add_row(str(index), hash.unique_id, hash.account, hash.password,
                      hash.date_created.strftime("%H:%M %B %d, %Y"))

    console.print(table)

# Base.metadata.create_all(engine)


if __name__ == "__main__":
    # Check if database exists here
    Base.metadata.create_all(engine)
    app()
