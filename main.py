from src.cli.argParser import main as argParser
from src.cli.art.asciiart import assci_logo

if __name__ == '__main__':
    print('\n' + assci_logo)
    argParser()
