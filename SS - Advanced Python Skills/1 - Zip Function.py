#Takes list, dicts, strings etc. and puts them into tuples
#used for parallel iteration
#returns a zip object - iterater of tuples

countries = ["UK", "USA", "Peru"]
caplitals = ["London", "Washigton", "Lima"]

#this is a object
contries_and_captials = zip(countries, caplitals)

#iterates through object - can only be done once not like array
print(contries_and_captials.__next__())


#good for parrallel iteration 
for counties, capitals in zip(countries, caplitals):
    print(counties, capitals)



#NOTES
#   -Will only be as long as the shortest list - opisite --> zip_longest()
#   -Can zip more than 2 elements into the tuple  
#   -Zipping Dict will zip the keys - .values() to zip values 
#   -Zipping Strings will zip each letter together
