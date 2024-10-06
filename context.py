import os


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

    def replace_temp_file(self) -> None:
        print("replace {0} with {1}".format(self.original_file, self.temp_file))
        os.remove(self.original_file)
        os.rename(self.temp_file, self.temp_file.replace("-temp", ""))