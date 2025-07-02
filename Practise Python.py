#Title - Practise Python
#Author - Alberto Campanero Arévalo
#Date - 2025-07-02
print("Hello, World!")
print("I+m learning Python! ")
print("I'm doing python exercises to learn the language.")
print ("When I want to get a variable value, I use the variable name with the = ")
print("For example, I'm going to create a new variable which will be called 'a'")
a = 5 
print(a)
print("Now, I'm going to create a list with some numbers.")
lista = [1, 2, 3, 4, 5]

print("The list is: " + str(lista))
print("Now, I'm going to use a for bucle")
for i in range(0, lista[4]):
    print(i)
    
print("Now, I'm going to use a method append")
lista.append(7)
print("The new list is: " +str(lista))

print("Now, I'm goint to use a dictionary")
dictionary = {"name": "Alberto",
              "age":30,
              "city": "Toledo",
              "job": "Programer"}
print("The dictionary is" +str(dictionary))

print("Just to finish, I'm going to use a set")
set_example = {1, 2, 3, 4, 5}
print("The set is: " + str(set_example))    
set_example2 = {5, 6, 7, 8, 9, 10,4 }
set = set_example | set_example2
print("If we want to get a union of two sets and we delete the repeated elements, we can use the | operator, example:")
print("The union of the two sets is: " + str(set))

print ("Different methods to work with python")
print("We use split to divide a string into a list of words")
print("We use append to add an element to a list")
print("We use joint to joint two strings")
print("We can use type to know the type of a variable")

#######################################################
print("Now, I'm going to use a compare operators")
print("We can use == to compare two variables")
print("We can use != to compare two variables") 
print("We can use < to compare two variables")
print("We can use > to compare two variables")      
print("We can use <= to compare two variables")
print("We can use >= to compare two variables")
print("We can use is to compare two variables")
print("We can use is not to compare two variables")     
print("We can use in to check if an element is in a list")
print("We can use not in to check if an element is not in a list")
print("We can use and to check if two conditions are true")
print("We can use || to check if one of two conditions is true")
print("We can use xor to check if one of two conditions is true, but not both")