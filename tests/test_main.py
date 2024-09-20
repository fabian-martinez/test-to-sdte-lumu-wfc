from typer.testing import CliRunner
from app.main import app 

runner = CliRunner()

def test_file_command_default(tmp_path):
    # Act
    result = runner.invoke(app, ["file","./tests/sample.txt"])
    # Assert
    assert result.exit_code == 0
    assert "{\"words\": 6, \"characters\": 25, \"kwd_density\": [[\"one\", 3], [\"two\", 2], [\"three\", 1]]}" in result.output

def test_file_command_plain(tmp_path):
    # Act
    result = runner.invoke(app, ["file","./tests/sample.txt","--format=plain"])
    # Assert
    assert result.exit_code == 0
    assert """6 words
25 characters

one: 3
two: 2""" in result.output

def test_file_command_histogram(tmp_path):
    # Act
    result = runner.invoke(app, ["file","./tests/sample.txt","--format=histogram"])
    # Assert
    assert result.exit_code == 0
    assert """6 words
25 characters

one    [3]  ****************************************
two    [2]  ***************************
three  [1]  **************""" in result.output

def test_text_command():
    # Act
    result = runner.invoke(app, ["text","One one two \none two three","--format=json"])
    # Assert
    assert result.exit_code == 0
    assert "{\"words\": 6, \"characters\": 25, \"kwd_density\": [[\"one\", 3], [\"two\", 2], [\"three\", 1]]}" in result.output