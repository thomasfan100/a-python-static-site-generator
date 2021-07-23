from pathlib import Path
import sys
class Site:
    """ has methods that help make the files/directories needed in parsed folder"""
    def __init__(self,source,dest,parsers = None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self,path):
        """
            makes a directory in dist
        """
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)

    def load_parser(self,extension):
        """
            takes all parsers and determines if valid
        """
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self,path):
        """
            loads and runs parser and performs parsing if found
            else, prints a fail message
        """
        #using self to run own class method
        #.suffix returns the extension name if any
        parser = self.load_parser(path.suffix)
        #is not vs !=
        if parser is not None:
            parser.parse(path,self.source,self.dest)
        else:
            self.error("No parser for the {} extension, file skipped!".format(path.suffix))

    def build(self):
        """
            uses create_dir to create new folders
        """
        self.dest.mkdir(parents = True, exist_ok = True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file() :
                self.run_parser(path)
    @staticmethod
    #static methods do not need to accept self
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n".format(message))
