import typer
from ssg.site import Site
import ssg.parsers

def main(source = "content", dest = "dist"):
    config = {
        "source" : source,
        "dest" : dest,
        "parsers" :[
            ssg.parsers.ResourceParser(),
            #md = markdown
            ssg.parsers.MarkdownParser(),
            #rst = restructured text
            ssg.parsers.ReStructuredTextParser(),
        ],
    }
    Site(**config).build()
typer.run(main)
