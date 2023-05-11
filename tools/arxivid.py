'''Provides a handle ArxivId for arXiv ids

'''

from .strtools import OpaqueStr

class ArxivId(OpaqueStr):

    @property
    def urls(self):
        return ArxivIdUrls(self._str)


class ArxivIdUrls(OpaqueStr):

    # TODO: Store these template strings elsewhere.
    # TODO: Refactor to reduce repetition.
    # TODO: Add docstrings to these properties.
    home = property('https://arxiv.org/abs/{._str}'.format)
    html_log = property('https://ar5iv.labs.arxiv.org/log/{._str}'.format)
    html = property('https://ar5iv.labs.arxiv.org/html/{._str}'.format)
    metadata = property('http://export.arxiv.org/api/query?id_list={._str}'.format)
    pdf = property('https://arxiv.org/pdf/{._str}'.format)
    source = property('https://arxiv.org/e-print/{._str}'.format)
