import os
from file_writter import write_to_file

def test_file_writter():
    test_filename = "test_output.txt"
    test_content = "test_content for ci"
    write_to_file(test_filename,test_content)

    os.path.exists(test_filename), "file not created"

    with open(test_filename, "r") as f:
        content = f.read()
        assert content == test_content , "file content does not match"

