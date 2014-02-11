from sys import argv
#Your job is to write a program named 'sorted_data.py' reads the file, 
#then spits out the ratings in alphabetical order by restaurant

#open the file
script, filename = argv

#read the file
f = open(filename, "r")
myfile = f.read()

#close the file
f.close()

split_lines = myfile.split("\n")

#make a dictionary
restaurants = {}
for line in split_lines:
    if ":" in line:
        #split line at ":"
        restaurant,rating = line.split(":")
        restaurants[restaurant] = rating

for key in sorted(restaurants.keys()):
    print "Restaurant %s has a rating of %s" % (key , restaurants[key])


