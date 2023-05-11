'''Provides a handle ArxivId for arXiv ids

'''

from .strtools import OpaqueStr

class ArxivId(OpaqueStr):

    @property
    def urls(self):
        return ArxivIdUrls(self._str)

    @property
    def dir_name(self):
        '''Name of directory for storing article data.
        '''

        raw_id = self._str

        old_style = bool('/' in raw_id)
        new_style = bool('.' in raw_id)
        if old_style + new_style != 1:
            raise ValueError(f'{self} is malformed')

        if old_style:
            return '__'.join(self._str.split('/'))
        elif new_style:
            return '_'.join(self._str.split('.'))
        else:
            raise ValueError('f{self}: This cannot happen!')


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
