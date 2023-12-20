#!/usr/bin/python3
"""Tests for the AirBnb clone modules.
"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears the contents of a given text stream.

    Args:
        stream (TextIO): The text stream to clear.
    """
    if stream.seekable():
        # Move the stream cursor to the beginning
        stream.seek(0)
        # Truncate the stream to remove existing content
        stream.truncate(0)


def delete_file(file_path: str):
    """Deletes a file if it exists.

    Args:
        file_path (str): The path of the file to be deleted.
    """
    if os.path.isfile(file_path):
        # Delete the file from the filesystem
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """Resets the items in the given store and file.

    Args:
        store (FileStorage): The FileStorage instance to reset.
        file_path (str): The path to the store's file.
    """
    with open(file_path, mode='w') as file:
        # Overwrite the file content with an empty dictionary
        file.write('{}')
        # Reload the store if it's provided
        if store is not None:
            store.reload()


def read_text_file(file_name):
    """Reads the contents of a text file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            # Read each line from the file and store in a list
            lines.extend(file.readlines())
    return ''.join(lines)


def write_text_file(file_name, text):
    """Writes text to a file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): The content to write to the file.
    """
    with open(file_name, mode='w') as file:
        # Write the provided text to the file
        file.write(text)
