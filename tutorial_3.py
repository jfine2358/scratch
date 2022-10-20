from lxml.etree import XMLParser
from lxml.etree import Resolver
from lxml.etree import parse

from tools import str_from_elt
from tools import FakeFile      # Note: Using FakeFile.

# TODO: Gotcha: AttributeError in resolver is suppressed.
class MyLookup(Resolver):

    def resolve(self, url, id, context):

        if url == 'book.xml':
            return None
        else:
            print(f'MyLookup resolving {url}.')
            value = f'<a>including {url}</a>'
            fakefile = FakeFile(value)
            return self.resolve_file(fakefile, context)


parser = XMLParser()
parser.resolvers.add(MyLookup())

print('''
#    book = parse('book.xml', parser)
#    print(str_from_elt(book))

#    book.xinclude()
#    print(str_from_elt(book))
''')
