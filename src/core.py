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
        
        # Get directory and filename
        file_dir = os.path.dirname(original_file)
        file_name = os.path.basename(original_file)
        name, format = file_name.rsplit(".", 1)
        
        # Create compressed directory in the same location as original file
        compressed_dir = os.path.join(file_dir, 'compressed')
        if not os.path.exists(compressed_dir):
            os.makedirs(compressed_dir)
        
        # Temp file goes to compressed directory
        self.temp_file = os.path.join(compressed_dir, "{0}-temp.{1}".format(name, format))
        self.final_file = os.path.join(compressed_dir, file_name)

        self.original_file_name = self.convert_file_name(self.original_file)
        self.temp_file_name = self.convert_file_name(self.temp_file)

    def set_format(self, format: str) -> None:
        """Change the output file format."""
        temp_name = os.path.basename(self.temp_file).rsplit(".", 1)[0]
        compressed_dir = os.path.dirname(self.temp_file)
        self.temp_file = os.path.join(compressed_dir, "{}.{}".format(temp_name, format))
        self.temp_file_name = self.convert_file_name(self.temp_file)
        
        # Update final file format as well
        final_name = os.path.basename(self.original_file).rsplit(".", 1)[0]
        self.final_file = os.path.join(compressed_dir, "{}.{}".format(final_name, format))

    def archive_original_file(self) -> None:
        """Archive is no longer needed - original file stays in place."""
        pass

    def delete_original_file(self) -> None:
        """Delete the original file."""
        if os.path.exists(self.original_file):
            os.remove(self.original_file)
        
    def rename_temp_file(self) -> None:
        """Rename temp file to final name in compressed directory."""
        os.rename(self.temp_file, self.final_file)


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
