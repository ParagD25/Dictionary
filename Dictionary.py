import json
import difflib

file=open('data.json')
content=json.load(file)

def find(word):
    if word.lower() in content:
        return content[word.lower()]
    elif word.title() in content:
        return content[word.title()]
    elif word.upper() in content:
        return content[word.upper()]
    elif len(difflib.get_close_matches(word,content.keys())):
        response=input(f'Did you mean \'{difflib.get_close_matches(word,content.keys())[0]}\' (Press \'Y\' to confirm or Press \'N\' to refuse) ---> ')
        if response.lower()=='y':
            return content[difflib.get_close_matches(word,content.keys())[0]]
        elif response.lower()=='n':
            return f'Cannot find \'{word}\' meaning'
        else:
            return 'Try Again!!'
    else:
        return 'The word \'%s\' does not exists , Please check !!!' %word
while True:
    word=input('Find the meaning of the word: ')
    result=find(word)
    if type(result)==list:
        length=len(result)
        print(f'Number of definitions found = {length}')
        if length==1:
            for val in result:
                print(f'Definition : {val}')
        else:
            for a,b in enumerate(result):
                print(f'Definition {a+1} : {b}')
    else:
        print(result)