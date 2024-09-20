import pytest
import json
from app.commands import read_file, read_text

def test_read_file(tmp_path):
    # Arrage
    file_path = tmp_path / "sample.txt"
    file_content = "One one two \none two three"
    file_path.write_text(file_content)
    expect_response = json.dumps(
        {'words':6,
         'characters':25,
         'kwd_density':
             [['one',3],['two',2],['three',1]]
             }
        )

    # Act
    result = read_file(str(file_path))
    
    # Assert
    assert result == expect_response


def test_read_text():
    # Arrage
    text = "One one two \none two three"
    expect_response = json.dumps(
        {'words':6,
         'characters':25,
         'kwd_density':
             [['one',3],['two',2],['three',1]]
             }
        )

    # Act
    result = read_text(text)
    
    # Assert
    assert result == expect_response


def test_read_non_txt_file(tmp_path):
    # Arrage
    file_path = tmp_path / "sample.pdf"
    file_path.write_text("Invalid File")

    # Act
    with pytest.raises(ValueError) as exc_info:
        read_file(str(file_path))
    
    # Assert
    assert "Invalid File Type" in str(exc_info.value)


def test_file_not_found():
    # Assert
    with pytest.raises(FileNotFoundError) as exc_info:
        read_file("not_found.txt")
    
    # Assert
    assert "File not found" in str(exc_info.value)