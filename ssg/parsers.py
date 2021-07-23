from typing import List
from pathlib import Path
import shutil

import sys
from docutils.core import publish_parts
from markdown import markdown
from ssg.content import Content


class Parser:
    """the purpose of a parser is to convert text from one file into the syntax of the other"""
    extensions:List[str] = []
    def valid_extension(self,extension):
        """
            checks if extension is valid
        """
        return extension in self.extensions

    def parse(self,path:Path,source:Path,dest:Path):
        """
            will be implemented by subclasses
        """
        raise NotImplementedError

    def read(self,path):
        """
            reads file and returns its contents
        """
        with open(path, "r") as file:
            return file.read()

    def write(self,path,dest,content,ext =".html"):
        """
            writes to a file with adjusted name
        """
        full_path = dest / path.with_suffix(ext).name
        with open(full_path,"w") as file:
            file.write(content)

    def copy(self,path,source,dest):
        """
            performs a file copy
        """
        shutil.copy2(path,dest/path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg",".png",".gif",".css",".html"]
    def parse(self,path,source,dest):
        """
            will just copy file to new destination because
            no parsing to new file type is needed.
        """
        self.copy(path,source,dest)

class MarkdownParser(Parser):
    extensions = [".md",".markdown"]
    def parse(self,path,source,dest):
        #content holds a content class with metadata and content
        content = Content.load(self.read(path))
        #uses mark library
        html = markdown(content.body)
        self.write(path,dest,html)
        #\x1b[1;32m changes string color to green
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name,content))

class ReStructuredTextParser(Parser):
    extensions = [".rst"]
    def parse(self,path,source,dest):
        content = Content.load(self.read(path))
        html = publish_parts(content.body,writer_name="html5")
        self.write(path,dest,html["html_body"])
        sys.stdout.write("\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name,content))
