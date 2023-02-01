class FileContext:
    original_file = None
    temp_file = None

    def __init__(self, original_file: str) -> None:
        self.original_file = original_file
        name, format = original_file.rsplit('.', 1)
        self.temp_file = "{0}-temp.{1}".format(name, format)
    
    def set_format(self, format: str) -> None:
        self.temp_file = "{}.{}".format(self.temp_file.rsplit('.', 1)[0], format)