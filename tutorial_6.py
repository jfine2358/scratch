from lxml.etree import XMLParser
from lxml.etree import Resolver
from lxml.etree import parse

from tools import str_from_elt
from tutorial_4 import catalog
from tutorial_5 import cat_blob

# TODO: Gotcha: AttributeError in resolver is suppressed.
class MyLookup(Resolver):

    def resolve(self, url, id, context):

        print(f'MyLookup resolving {url}')
        git_oid = catalog[url]
        
        value = f'<a>including {url}</a>'
        fakefile = cat_blob('mybook', git_oid)
        return self.resolve_file(fakefile, context)


parser = XMLParser()
parser.resolvers.add(MyLookup())

print('''\
#    book = parse('book.xml', parser)
#    print(str_from_elt(book))

#    book.xinclude()
#    print(str_from_elt(book))
''')
