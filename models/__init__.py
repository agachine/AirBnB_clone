#!/usr/bin/python3
"""
Entry point for the AirBnB console
"""
from models.engines.file_storage import FileStorage

storage = FileStorage()
storage.reload()

