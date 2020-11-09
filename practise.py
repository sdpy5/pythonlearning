favourite_language = {'jen' : ['python','ruby'],
'sarah' : ['c'],
'edward' : ['ruby','go'],
'phil' : ['python','haskel']}

for name,languages in favourite_language.items():
    print('the names are : ' + name.title())
    for language in languages:
        print('\t' + language)
