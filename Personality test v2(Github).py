# Personality Test- attributes numbers to personality traits and tells the user their personality
# Questions
# user name
#instructions for the test--------------------------------------------------------------------------------------------------------------------------------------------
test_taker_name=input("Enter your name:")
print("Please enter if the following is like you, 1 being more like you 2 being neutral and 3 being least like you:")
#question 1-----------------------------------------------------------------------------------------------------------------------------------------------------------
question_1 = int(input(
    "I enjoy being by myself more than I like going to a huge party or gathering: "))
question_1_awnser = question_1
while question_1_awnser>3 or question_1_awnser<0:
    print("Error, please enter an awnser that is between the numbers one and three")
    question_1_awnser= int(input(
    "I enjoy being by myself more than I like going to a huge party or gathering: "))
print("Thank you for that.")
#Question 2---------------------------------------------------------------------------------------------------------------------------------------------------------------
question_2 = int(
    input("I like curling up with a good book even if I am at a huge party:"))
question_2_awnser = question_2
while question_2_awnser<1 or question_2_awnser>3:
    print("Error, please enter an awnser that is between the numbers one and three")
    question_2_awnser = int(input(
        "I like curling up with a good book even if I am at a huge party:"))
print("Thank you for your input.")
#Question 3--------------------------------------------------------------------------------------------------------------------------------------------------------
question_3 = int(input(
    "I think that time alone is really peaceful and is better than going out:"))
question_3_awnser = question_3
while question_3_awnser>3 or question_3_awnser<1:
    print("Error, please enter an awnser that is between the numbers one and three")
    question_3_awnser = int(input(
        "I think that time alone is really peaceful and is better than going out:"))
print("Thank you for your awnser")
# this will add up the awnsers and calculate what kind of personality you have---------------------------------------------------------------------------------
total_of_personality = question_1_awnser+question_2_awnser+question_3_awnser
print("Currently calculating personality.")
if total_of_personality == 3:
    print(test_taker_name, "You seem most likely to have alot of strong introverted tendencies, good for you you are more likely to be more reflective.")
elif total_of_personality == 6:
    print(test_taker_name, "You seem like a ambivert, you can feel comfortable with going to parties or just being by yourself!")
elif total_of_personality == 9:
    print(test_taker_name,
          "You're seem like an extravert who loves being around people and feeling their energy!")
else:
    print(test_taker_name,
          "You have such a unique personality that it can't be determined by a test.")
