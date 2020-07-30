# --------------
class_1 = [ 'Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = [ 'Hilary Mason','Carla Gentry','Corinna Cortes']

# combine both lists
new_class = class_1+class_2
print(new_class)

# add a new element in the list
new_class.append('Peter Warden')
print(new_class)

# remove a member from the list
new_class.remove('Carla Gentry')
print(new_class)

# create a dictionary

courses = {'Math' : 65, 'English' : 70, 'History': 80, 'French'	: 70, 'Science' : 60}

# Add the values of the dictionary
total = sum(courses.values())
print(total)

# print the percentage of all the subject marks
percentage = total/5
print(percentage)

# crete a dictionary 
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70}

# print the name of the topper
topper = max(mathematics,key = mathematics.get)
print(topper)


#  first_name 
first_name = (topper.split()[0])
print (first_name)

#  Last_name
last_name = (topper.split()[1])
print (last_name)

# add the first name and last name
full_name = last_name + ' ' + first_name

# print the full_name
print (full_name)

# name in upper case
certificate_name = full_name.upper()

print (certificate_name)





