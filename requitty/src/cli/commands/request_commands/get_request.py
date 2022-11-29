import requests
import json

def main(params):

    if 'get' in params.request:
        try:
            response = requests.get(params.url)
            response_decoded = response.json()

            ###############################################
            #######          ALL IS OK            #########
            ###############################################
          
            if response.status_code >= 200 and response.status_code < 299: #If the status code is Ok 
                
                if params.verbose: #If verbose is true in params print the response
                    print(response_decoded)
                print(f'\n Succes and exit with {response.status_code}')
            


            ###############################################
            ####          ERROR STATUS CODE          ######
            ###############################################
                
            elif response.status_code >= 400 or response.status_code >= 599:
                print(f'\n Not found exit with {response.status_code} \n response: {response_decoded}' )
                return response.status_code
        except:
            print("\n Error was ocurred, check url and try again")
            return 500


if __name__ == '__main__':
    main()
