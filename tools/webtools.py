'''Tools related to web requests

We use only the Python standard library.

'''

from urllib.error import HTTPError
from urllib.request import build_opener
from urllib.request import HTTPRedirectHandler
from urllib.request import urlopen


def get_random_arxiv_id():

    # This URL will redirect to a random arxiv article.
    lucky = 'https://ar5iv.labs.arxiv.org/feeling_lucky'

    # Get the location (assumed relative) for the random article.
    location = get_redirect_location(lucky)

    # Strip the prefix from the location to get arxiv_id.
    if not location.startswith('/html/'):
        raise ValueError
    else:
        arxiv_id = location[len('/html/'):]

    # All done.
    return arxiv_id


def get_redirect_location(url):
    '''If possible return redirect location, else raise ValueError.

    The returned value is the redirect location, as provided in the
    response to the provided URL. The redirect location is not
    followed.
    '''

    # We need a url opener that does not follow a redirect.
    # To understand this, read the docs for urllib.request.
    opener = build_opener(DontRedirect)

    # TODO: Perhaps be more particular about the response.
    try:
        request = opener.open(url)
    except HTTPError as redirect:
        return redirect.headers['location']

    raise ValueError(f'{request} is not a redirect')


class DontRedirect(HTTPRedirectHandler):
    '''A redirect handler that doesn't follow the redirect.'''

    # See the docs for urllib.request.
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None
