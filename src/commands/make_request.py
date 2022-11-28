import requests


def main(params):

    """
     Make a get request using the given url in args and return a respose with data 
     if verbose is true, if verbose isnt true return a succes message.
    """

    if 'get' in params.request[0]:
        try:
            response = requests.get(params.request[1])

            if response.status_code == 200:
                if params.verbose:
                    return response.json(), response.status_code
                return 'Succes'
            else:
                return 'Error was ocurred o url is not valid'
        except:
            return 'Error was ocurred'


if __name__ == '__main__':
    main()
