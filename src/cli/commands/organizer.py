from colorama import Fore, init
from tqdm import tqdm
from time import sleep
from src.constants import extension
import os 

init(autoreset=True)


def main(params):
    try:

        dirList = os.listdir(params.order)        

        if params.verbose:
            pbar = tqdm(dirList)
            for i in pbar:
                sleep(0.01)
                pbar.set_description(f'Loading data: {i}')

        for i in dirList:
            if i.split('.')[-1] in extension['video']:
                print(i)






    except:
        print(Fore.RED + 'the path is incorrect')

if __name__ == '__main__':
    main()