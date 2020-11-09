favourite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
voters = ['jen','sarah','sangith','edward','phil','shravanya']
for voter in voters:
    if voter in favourite_languages.keys():
        print('thanks for taking the poll ' + voter)
    else:
        print('please take the poll ' + voter)