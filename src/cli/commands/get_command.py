import os
from tqdm import tqdm
from colorama import Fore, init
from time import sleep
from json import dump
from requests import get

# Inicializamos la librería colorama para poder utilizar colores en la consola
init(autoreset=True)

def main(params) -> None:
    # Definimos una función interna llamada save que se encargará de guardar la respuesta en un archivo
    def save(response_name) -> None:
        # Intentamos abrir un archivo para escribir en él la respuesta
        try:
            with open(f"data/{response_name}.json", "w") as file:
                # Utilizamos la función dump de json para escribir la respuesta en formato JSON en el archivo
                dump(response_decoded, file)
                file.close()
            # Si todo ha ido bien, mostramos un mensaje de éxito
            print(Fore.GREEN +f"\n Data saved successfully")
        except:
            # Si ocurre algún error al crear o escribir en el archivo, mostramos un mensaje de error
            print(Fore.GREEN + f"Error was ocurred when try to create the file {response_name}")
            return

    # Si se ha indicado en los parámetros que se debe realizar una petición GET
    if 'GET' in params.request:
        # Intentamos realizar la petición
        try:
            response = get(params.url)
            # Decodificamos la respuesta en formato JSON
            response_decoded = response.json()

            # Si la petición ha tenido éxito (es decir, si el código de estado de la respuesta es 2xx)
            if response.status_code >= 200 and response.status_code < 299:
                # Utilizamos la librería tqdm para mostrar una barra de progreso mientras se cargan los datos
                pbar = tqdm(response_decoded)
                for i in pbar:
                    sleep(0.01)
                    pbar.set_description(f'Loading data: {i}')

                # Si se ha indicado en los parámetros que se deben mostrar más detalles (parámetro verbose), mostramos la respuesta completa
                if params.verbose:  
                    print(response_decoded)
                # Mostramos un mensaje de éxito y el código de estado de la respuesta
                print(Fore.GREEN + f'\n Succes and exit with {response.status_code} \n')



                ###############################################
                #######          SAVE DATA            #########
                ###############################################

                """
                It is looking for, saves the response provided by the GET method, a new file is created and if there is one with the same name, it asks again how the file will be named
                """

                if params.save: 
                    if not os.path.exists(os.getcwd() + '/data'): 
                        os.mkdir(os.getcwd() + '/data')

                    response_name = input("\n input a name file: ")

                    #Save the response and prove if the name already exists

                    while os.path.exists(os.getcwd() + f'/data/{response_name}.json'):
                        response_name = input(" Response file exists input name file: ")
                    save(response_name)




            ###############################################
            ####          ERROR STATUS CODE          ######
            ###############################################

            elif response.status_code >= 400 or response.status_code >= 599:
                print(
                    Fore.YELLOW + f'\n Not found exit with {response.status_code} \n response: {response_decoded} \n ')
                return response.status_code
        except:
            print(Fore.RED + "\n Forced close \n ")
            return


if __name__ == '__main__':
    main()
