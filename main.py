import cyrtranslit as cyr
import argparse as arg

from autocorrect import Speller

def main():
    parser=arg.ArgumentParser(description='Cyrillic to latin converter')
    parser.add_argument('-l','--lang',
                        help='Specifies the language used for the translation',
                        default='sr')
    args=parser.parse_args()
    lang=args.lang
    
    langList=cyr.supported()

    if lang not in langList:
        print("Language isn't supported")
        quit()

    text=input('Enter some cyrillic: ')
    text=cyr.to_latin(text,lang)

    spell=Speller()

    print('Translated to latin:',spell(text))

if __name__ == '__main__':
    main()