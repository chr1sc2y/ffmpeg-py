import os
import shutil

class FileContext:
    original_file = None
    temp_file = None
    original_file_name = None
    temp_file_name = None

    def convert_file_name(self, name):
        return name.replace(" ", "\\ ").replace("'", "\\'")

    def __init__(self, original_file: str) -> None:
        self.original_file = original_file
        name, format = original_file.rsplit(".", 1)
        self.temp_file = "{0}-temp.{1}".format(name, format)

        self.original_file_name = self.convert_file_name(self.original_file)
        self.temp_file_name = self.convert_file_name(self.temp_file)

    def set_format(self, format: str) -> None:
        self.temp_file = "{}.{}".format(self.temp_file.rsplit(".", 1)[0], format)
        self.temp_file_name = self.convert_file_name(self.temp_file)

    def archive_original_file(self) -> None:
        # print("archive original file {0}".format(self.original_file))

        file_prefix = os.path.dirname(self.original_file)
        archive_dir = os.path.join(file_prefix, 'archive')
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
        destination = os.path.join(archive_dir, os.path.basename(self.original_file))
        shutil.move(self.original_file, destination)
        # print(f"File {self.original_file} has been moved to {destination}")

    
    def rename_temp_file(self) -> None:
        # print("rename temp file {0}".format(self.temp_file))
        os.rename(self.temp_file, self.temp_file.replace("-temp", ""))