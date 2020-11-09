# pythonlearning

Repository made for study purpose

Dictionary

             A dictionary in python is a collection of keyvalue pairs.Each key is connected to a value and you can use a key to access the value associated with that key.
a key's value can be a number,a string,a list,or even another dictionary.

1. In python,a dictionary is wrapped with {} braces with a series of key-value pairs

2. example :  alien = {'color' : 'red','points' : 5} #here 'color' & 'points' are the keys and 'red' & 5 are the values assigned to the keys
              every key is connected to its value by a colon ':'.

3. Accessing values in a dictionary
   example : alien = {'color' : 'red','points' : 5}
             print(alien['color'])

             output : red

4. The accessed keys can be assigned to a variable for further use

5. Adding new key-value pairs
    example : alien = {'color' : 'red','points' : 5}
              alien['speed'] = 'medium'
              print(alien)

              output : {'color': 'red', 'points': 5, 'speed': 'medium'}

6. Modifying values
    example :  alien = {'color' : 'red','points' : 5}
               print(alien)
               alien['color'] = 'blue'
               print(alien)          

               output : {'color' : 'red','points' : 5}
                        {'color' : 'blue','points' : 5}

7. By changing one value in the dictionary, you can change the overall behavior of the program

8. Removing key-value pairs 
    example : alien = {'color' : 'red','points' : 5}
              print(alien)
              del alien['color]
              print(alien)

              output : {'color' : 'red','points' : 5}
                       {'points' : 5}
    note : be aware that the deleted key-value pair is removed permanently

9. A dictionary of similar items
    example : favourite_language = {
                      'jen' : 'c',
                      'sangith' : 'python',
                      'shravanya' : 'java',
                      'sushagh' : 'ruby',
                      }
               print('shravanyas favourite language is '  + favourite_language['shravanya'].title() + '.')

               output : shravanyas favourite language is Java.