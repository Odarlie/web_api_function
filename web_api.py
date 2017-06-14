from urllib.request import urlopen, Request, URLError
import json


def web_url(url):
    """
      function that accepts an API
    """

    request = Request(url)

    try:
        response = urlopen(request)
        result = json.loads(response.read().decode('utf-8'))

    except URLError as error:
        return {"Error": str(error)}

    else:
        return result['city']['country']
