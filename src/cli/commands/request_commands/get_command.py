from tqdm import tqdm
from colorama import Fore, init
import json, requests, time, os


init(autoreset=True)


def main(params):
    if 'GET' in params.request:
        try:
            response = requests.get(params.url)
            response_decoded = response.json()

            ###############################################
            #######          ALL IS OK            #########
            ###############################################

            if response.status_code >= 200 and response.status_code < 299:

                pbar = tqdm(response_decoded)
                for i in pbar:
                    time.sleep(0.1)
                    pbar.set_description(f'Loading data: {i}')

                if params.verbose:  # If verbose is true in params print the response
                    print(response_decoded)
                print(Fore.GREEN + f'\n Succes and exit with {response.status_code} \n')

                if params.save:
                    print(os.getcwd())
                    




            ###############################################
            ####          ERROR STATUS CODE          ######
            ###############################################

            elif response.status_code >= 400 or response.status_code >= 599:
                print(
                    Fore.YELLOW + f'\n Not found exit with {response.status_code} \n response: {response_decoded} \n ')
                return response.status_code
        except:
            print(Fore.RED + "\n Error was ocurred, check the url \n ")
            return


if __name__ == '__main__':
    main()
