import re
# The FullLoader parameter handles the conversion from YAML
# scalar values to Python the dictionary format
from yaml import load,FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter,re.MULTILINE)

    @classmethod #decorator
    def load(cls,string):
        """
            pre: string is the file text contents
            post: returns an object of the class set with metadata and content

        """
        #splits the YAML frontmatter (delimited by --- or +++)
        #and the rest of the file
        _,fm,content = cls.__regex.split(string,2) #depth of 2
        #metadata gets the frontmatter in dict format
        #example: {'type': 'post', 'title': 'Code', 'author': 'PS Demo', 'date': '01-28-2020'}
        metadata = load(fm,Loader = FullLoader)
        return cls(metadata,content)

    def __init__(self,metadata, content):
        self.data = metadata
        self.data["content"] = content #key value pair

    @property
    def body(self):
        """ getter for the body content """
        return self.data["content"]

    @property
    def type(self):
        """ getter for the body type """
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self,type):
        """ setter for the body type """
        self.data["type"] = type

    def __getitem__(self,key):
        """
            abstract method of map
            can get type or content depending on key val
        """
        return self.data[key]

    def __iter__(self):
        """ abstract method of map that calls self iteration method """
        self.data.__iter__()

    def __len__(self):
        """ abstract method of map that returns length of self.data """
        return len(self.data)

    def __repr__(self):
        """ creates a custom representation of self.data """
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)
