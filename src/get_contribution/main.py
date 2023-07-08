from get_contribution.utilities import *
import uuid
import typer
from typing import Optional

EXIT_FAILURE = 1
DEFAULT_FILENAME = f'{uuid.uuid4().hex[:6]}.txt'

app = typer.Typer()

@app.command()
def main(username: Optional[str] = typer.Argument(default=None)):
    if get_log(DEFAULT_FILENAME) == 1:
        raise typer.Exit(EXIT_FAILURE)

    if username is None:
        day_map = process_log(DEFAULT_FILENAME)
    else:
        day_map = process_log(DEFAULT_FILENAME, username)
    
    total_coding_time = get_total_coding_time(day_map=day_map)

    format_coding_time(total_coding_time)

    clean_up(DEFAULT_FILENAME)

if __name__ == "__main__":
    app()