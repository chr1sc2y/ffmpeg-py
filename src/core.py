import os
import shutil
from typing import Callable
from pathlib import Path


class FileContext:
    """Context manager for file processing with automatic temp file handling."""
    
    original_file = None
    temp_file = None
    original_file_name = None
    temp_file_name = None

    def convert_file_name(self, name):
        """Escape special characters in file names for shell commands."""
        return name.replace(" ", "\\ ").replace("'", "\\'")

    def __init__(self, original_file: str) -> None:
        self.original_file = original_file
        name, format = original_file.rsplit(".", 1)
        self.temp_file = "{0}-temp.{1}".format(name, format)

        self.original_file_name = self.convert_file_name(self.original_file)
        self.temp_file_name = self.convert_file_name(self.temp_file)

    def set_format(self, format: str) -> None:
        """Change the output file format."""
        self.temp_file = "{}.{}".format(self.temp_file.rsplit(".", 1)[0], format)
        self.temp_file_name = self.convert_file_name(self.temp_file)

    def archive_original_file(self) -> None:
        """Move original file to archive subdirectory."""
        file_prefix = os.path.dirname(self.original_file)
        archive_dir = os.path.join(file_prefix, 'archive')
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
        destination = os.path.join(archive_dir, os.path.basename(self.original_file))
        shutil.move(self.original_file, destination)

    def delete_original_file(self) -> None:
        """Delete the original file."""
        if os.path.exists(self.original_file):
            os.remove(self.original_file)
        
    def rename_temp_file(self) -> None:
        """Rename temp file to final name by removing -temp suffix."""
        os.rename(self.temp_file, self.temp_file.replace("-temp", ""))


def traverse(
    dir: str, format: str, func: Callable, var1=None, var2=None, var3=None, recursive=False
) -> None:
    """
    Traverse directory and process files matching the given format.
    
    Args:
        dir: Directory path to traverse
        format: File extension to match (e.g., ".mp4", ".jpg")
        func: Processing function to call for each matching file
        var1, var2, var3: Parameters to pass to the processing function (function-specific)
        recursive: If True, recursively process subdirectories
    """
    directory = Path(dir)
    try:
        for obj in directory.iterdir():
            obj_relative_path = os.path.join(dir, obj)
            if not os.path.isfile(obj_relative_path):
                # Only recurse into subdirectories if recursive=True
                if recursive:
                    traverse(obj_relative_path, format, func, var1, var2, var3, recursive)
            elif obj_relative_path.lower().endswith(format.lower()):
                ctx = FileContext(obj_relative_path)
                func(ctx, var1, var2, var3)
    except (OSError, IOError) as e:
        print(f"⚠️  Skip unaccessible dir: {directory}\nError info: {e}")
