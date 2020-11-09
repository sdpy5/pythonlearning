#using dictionaries inside a dictionary



users = {
    'sangith dharshan':{
        'firstname':'sangith','lastname':'dharshan','location':'bangalore'},
    'shravanya':{
        'firstname':'shravanya','lastname':'sunildas','location':'bagalgunte'},
    'sushagh':{
        'firstname':'sushagh','lastname':'somarajan','location':'kannur'
    },    
}

for usernames,user_details in users.items():
    print('the user name is >>> ' + usernames.title())
    fullname = user_details['firstname'] + user_details['lastname']
    location = user_details['location']
    print('\tusers full name is >>>> ' + fullname.title())
    print('\tusers location is >>>> ' + location.title())

    
    #output
    
the user name is >>> Sangith Dharshan
        users full name is >>>> Sangithdharshan
        users location is >>>> Bangalore
the user name is >>> Shravanya
        users full name is >>>> Shravanyasunildas
        users location is >>>> Bagalgunte
the user name is >>> Sushagh
        users full name is >>>> Sushaghsomarajan
        users location is >>>> Kannur
    
