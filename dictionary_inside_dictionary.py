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