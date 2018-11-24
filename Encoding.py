#function 1
#will read, then encode a string,then split string into a list and turn it into
#a dictionary where the value is based on the characters.
#Then save to file

#first have string read from user
#lowercase the string
#replace vowels with different symbol
#then generate a random number in a certain range, and do modulo length of string
#find character at index equal to result
#split string using character as delimiter
#add character to end of list
#save list to file
#turn list into dictionary, where the value for each key is the number of vowels in the key
#sum values using for loop, print total number of vowels

#function 2
#read file and decode string

#main code
#ask for user to enter: encode, decode or end.
#call appripriate function or end

import random

def encode():
    message = input("Please enter the message to be encoded. Please do not use any semi colons")
    message = message.strip() #remove excessive whitespace and semi colons and set all characters to lower case
    message =message.strip(";")
    message =message.lower()
    message =message.replace("a","Zv") #Z marks presence of vowel. lowercase letter after is for decoding to correct vowel
    message =message.replace("e","Zw")
    message =message.replace("i","Zx")
    message =message.replace("o","Zy")
    message =message.replace("u","Zz")
    index = random.randint(5,100)%len(message) #by using modulo of length of message, it is certain to produce a valid index
    character = message[index]
    message_list = message.split(character)
    message_list.append(character)
    encoded_string = ";".join(message_list)
    with open("Encoded Message.txt", "w") as doc: #with will ensure that the document opened will be closed at the end of the indentation
        doc.write(encoded_string)
    vowels_per_element = []
    for element in message_list: #make a list of the number of vowels in each element of the split message
        count = 0
        for letter in element:
            if letter == "Z":
                count += 1
        vowels_per_element.append(count)
    dictionary = {key:value for key,value in zip(message_list, vowels_per_element)}
    total_vowels = 0
    for i in dictionary.values():
        total_vowels += i
    print("The total number of vowel in your message was "+str(total_vowels))


def decode():
    try:
        with open("Encoded Message.txt") as doc:
            encoded_message = doc.read()
        encoded_message_list = encoded_message.split(";")
        split_character = encoded_message_list.pop()
        decoded_message = split_character.join(encoded_message_list)
        decoded_message = decoded_message.replace("Zv","a") #as the vowel markers are the only uppercase letters, none of the non-vowels will be accidently replaced
        decoded_message = decoded_message.replace("Zw","e")
        decoded_message = decoded_message.replace("Zx","i")
        decoded_message = decoded_message.replace("Zy","o")
        decoded_message = decoded_message.replace("Zz","u")
        print("The encoded message is: "+decoded_message)
    except FileNotFoundError: #prevents the program from crashing if the user tries to decode before encoding anything
        print("There is no encoded message")

choice = ""
while choice!= "end":
    choice = input("Please type encode, decode, or end to select the desired process")
    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    elif choice != "end":
        print("That is not a valid instruction")








