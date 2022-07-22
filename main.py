import cyrtranslit as cyr
from autocorrect import Speller

def main():
    text=input('Enter some cyrillic: ')
    text=cyr.to_latin(text,'ru')

    spell=Speller()
    
    print('Translated to latin:',spell(text))

if __name__ == '__main__':
    main()