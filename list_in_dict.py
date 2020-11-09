classes = {
    'teachers' : 'srinivas murthy',
    'students' : ['sangith','dharshan','sushagh','shravanya']
}

print('the class teacher is : ' + classes['teachers'] + '.')
print('the students are : ')
for student in classes['students']:
    print('\t' + student.title())
    if student == 'sushagh':
        print('sushagh is the favourite student')
        