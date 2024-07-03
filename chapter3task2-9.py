# secret word variable
secret_word = "chupacabra"

# expression to allow the user to input a guess
word_guess = str(input("Please enter the secret word:"))    


# while loop initiated
while word_guess != secret_word:
    
    if word_guess == secret_word:
        break
    word_guess = str(input("Please enter the secret word again:"))
    
# string output when word has been guessed
print ("you've successfully left the loop.")