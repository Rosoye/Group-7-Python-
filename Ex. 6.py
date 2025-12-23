#The line below states that there are 10 types of people using types_of_people as a variable
types_of_people = 10
#The f before the string is used to apply format to a string. It applies the variable above in a string. This is all under a variable x
x = f"There are {types_of_people} types of people." 

#This line below states a string; binary under a variable; binary
binary = "binary"
#The line below states a string; don't under a variable; do_not
do_not = "don't"
#The f before the string is used to apply format to a string. It applies the variables above in a string thereby causing their respective strings to be represented. This is all under a variable y
y = f"Those who know {binary} and those who {do_not}."

#The line below shows the execution of the variable x above
print(x)
#The line below shows the execution of the variable y above
print(y)

#This means to run the string below which also applies the variable, x above
print(f"I said: {x}")
#This means to run or print the string below which also applies the variable, y above
print(f"I also said: '{y}'")

#This line below states a value; False under a variable; hilarious
hilarious = false
#This line below states a string; 'Isn't that joke so funny?! {}' under a variable; joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"
 
#This line below shows the running of the variables above
print(joke_evaluation.format(hilarious))

#This line below states a string; 'This is the left side of...' under a variable; w
w = "This is the left side of..."
#This line below states a string; 'a string with a right side.' under a variable; e
e = "a string with a right side."
#The line shows the execution of the two variables above
print(w + e)


#There are five places where a string is put inside a string which are lines 11, 19, and 21
#No. In line 11, variable {binary}, which represented string binary, was put in a string y
#Also in line 11, variable {do_not}, which represented string don't, was put in a string y
#In line 19, variable {x}, which represented string 'There are {types_of_people} types of people.', was put in another string
#In line 21, variable {y}, which represented string 'Those who know {binary} and those who {do_not}.', was put inside a string which was also put inside another string which made it twice

#The symbol + is seen as concatenation which helps to join strings w and e together.