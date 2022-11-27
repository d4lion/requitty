import requests
import json



def main(params):



    if 'get' in params.request:
        try:
            response = requests.get(params.url[0])
            if (params.verbose != None):
                print(response.json())

        except:
            print('The url is not valid')


if __name__ == '__main__':
    main()
