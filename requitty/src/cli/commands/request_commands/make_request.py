import requests


def main(params):

    if 'get' in params.request:
        try:
            response = requests.get(params.url)

            ###############################################
            #######          ALL IS OK            #########
            ###############################################
          
            if response.status_code >= 200 and response.status_code < 299: #If the status code is Ok 
                
                if params.verbose: #If verbose is true in params print the response
                    print( response.json(), response.status_code)
                print('Succes')





            ###############################################
            ####          ERROR STATUS CODE          ######
            ###############################################
                
            elif response.status_code == 404:
                print('Not found')
                return 1
            elif response.status_code == 500:
                print('Internal server error')
                return 1
            else:
                print('Error was ocurred o url is not valid')
                return 1
        except:
            return 'Error was ocurred'


if __name__ == '__main__':
    main()
