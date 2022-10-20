from lxml.etree import XMLParser
from lxml.etree import Resolver
from lxml.etree import parse

from tools import str_from_elt


# TODO: Gotcha: AttributeError in resolver is suppressed.
# With: f'{self.__name__} etc'
# Get: lxml.etree.XIncludeError: could not load front.xml, and no fallback was found

class MyLookup(Resolver):

    def resolve(self, url, id, context):

        print('Entering MyLookup ...')
        if url == 'book.xml':
            print('... skipping.')
            return None
        else:
            print(f'... resolving {url}.')
            value = f'<a>[including {url}]</a>'
            return self.resolve_string(value, context)


parser = XMLParser()
parser.resolvers.add(MyLookup())

print('''
#    book = parse('book.xml', parser) # Note: parser arg.
#    print(str_from_elt(book))

#    book.xinclude()
#    print(str_from_elt(book))
''')
