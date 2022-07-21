import cyrtranslit as cyr

def main():
    text=input('Enter some cyrillic: ')
    text=cyr.to_latin(text,'ru')
    print('Translated to latin:',text)

if __name__ == '__main__':
    main()