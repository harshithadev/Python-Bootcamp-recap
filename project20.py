# Project 20 : String Formatting 

# given two lists with names and their respective marks, we must format it in a way thay it looks presentable. 

names = ["Harshitha", "Barath", "Koush", "Jay", "Guru"]
marks = [100, 90, 80, 70, 100]
# this maps the person with their respective marks.
names = zip(names, marks)
print('{0:<10} {1:<3}'.format("Names", "Marks"))
for person in names : 
    print('{0:<10} {1:<3}'.format(person[0], person[1]))
