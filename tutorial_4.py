# TODO: Explain how to create mybook git repos.
# TODO: Explain use of git cat-file.
cat_file_output = '''\
3e1ba222b3a47b0d54fd966b6ba2e976c348e92e back.xml
b7ef266514be61ae088f9ba9bfd5d3858078bfaa body.xml
1273412999fc3c620ddbe8466ebeea8050e5422f book.xml
e4c9d75983abe42a21e55f08190681f436079ac5 front.xml
'''

data = cat_file_output.split()

items = iter(data)

# Create a (name, git_oid) catalog.
catalog = {}
for val, key in zip(items, items):
    catalog[key] = val


if __name__ == '__main__':
    print('''\
#    print(data)
#    print(catalog)
''')
