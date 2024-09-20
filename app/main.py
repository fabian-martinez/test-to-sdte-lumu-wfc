import typer
from commands import read_file,read_text


app = typer.Typer()

@app.command()
def file(file_path: str, format='json'):
    print(f"{read_file(file_path,format)}")

@app.command()
def text(text: str, format='json'):
    print(f"{read_text(text,format)}")

if __name__ == "__main__":
    app()