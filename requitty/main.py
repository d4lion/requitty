from src.args import request, url, save 
from src.cli.commands.request_commands import get_request

import argparse


def main():
    parser = argparse.ArgumentParser(prog='requitty')


    ###############################################
    ####          REQUEST ARGUMENT           ######
    ###############################################

    parser.add_argument(request['shortCommand'], metavar=request['longCommand'], help=request['help'], dest="request", type=str)

    parser.add_argument(url['shortCommand'], metavar=url['longCommand'], help=url['help'], type=str, dest="url")
    

    parser.add_argument("-v", help="Make a verbose script", type=bool, default=False, metavar="--verbose", dest="verbose")

    parser.add_argument(save['shortCommand'], metavar=save['longCommand'], help=save['help'], type=bool, default=False, dest='save')

    args_parse = parser.parse_args()

    if args_parse.request:
        get_request.main(args_parse)

if __name__ == '__main__':
    main()
