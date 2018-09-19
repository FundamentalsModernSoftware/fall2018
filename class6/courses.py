allCourses = {'jtg243': ['NBAY 5400', 'LAW 6512'], 
              'sjb344': ['CS 5785'], 
              'vk342': ['ECE 5410', 'ECE 5411']}

for prof in allCourses:
    profsCourses = ' and '.join(allCourses[prof])
    print (prof + ' is teaching ' + profsCourses)

