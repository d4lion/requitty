from src.constants import request, url, save, sort
from src.cli import asciiart
from src.cli.commands import get_command
from src.cli.commands import organizer
from os import getcwd as cwd
import argparse


def main():
    parser = argparse.ArgumentParser(prog="")

    ###############################################
    ####          REQUEST ARGUMENT           ######
    ###############################################

    parser.add_argument(request['shortCommand'], metavar=request['longCommand'],
                        help=request['help'], dest="request", type=str)

    parser.add_argument(url['shortCommand'], metavar=url['longCommand'], help=url['help'],
                        type=str, dest="url", default="https://rickandmortyapi.com/api")

    parser.add_argument("-v", help="Make a verbose script", type=bool,
                        default=False, metavar="--verbose", dest="verbose")

    parser.add_argument(save['shortCommand'], metavar=save['longCommand'],
                        help=save['help'], type=bool, default=False, dest='save')

    ###############################################
    ####          REQUEST SYSTEM             ######
    ###############################################

    parser.add_argument(sort['shortCommand'], help=sort['help'],
                        metavar=sort['longCommand'], type=str, dest='order')

    args_parse = parser.parse_args()

    if args_parse.request:
        get_command.main(args_parse)

    if args_parse.order:
        organizer.main(args_parse)


if __name__ == '__main__':
    print('\n' + asciiart.assci_logo)
    main()
