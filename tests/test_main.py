from typer.testing import CliRunner
from app.main import app 

runner = CliRunner()

def test_file_command(tmp_path):
    # Act
    result = runner.invoke(app, ["file","./tests/sample.txt"])
    # Assert
    assert result.exit_code == 0
    assert "Goodbye Alice" in result.output

def test_text_command():
    # Act
    result = runner.invoke(app, ["text","One one two \none two three"])
    # Assert
    assert result.exit_code == 0
    assert "Goodbye Alice" in result.output