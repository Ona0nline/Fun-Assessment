def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """
    
    h_age = int(input("Enter dogs age:\n"))
    d_age_2 = h_age * 5.25
    d_age_after = ((h_age - 2) * 4) + 21
    
    if h_age <= 2:
        print(f"The dog's age in dog's years is {d_age_2}")
    
    elif h_age > 2 and h_age <= 20:
        print(f"The dog's age in dog's years is {d_age_after}")
    else:
        print("Your dog is either not born yet or it is dead :( ")
        
    
    #enter your code here

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here

    
    # for index in range(1,num):
        
    #     if index % 3 == 0 and index % 5 == 0:
    #         index = "FizzBuzz"
    #     print(index)
        
    #     if index % 5 == 0:
    #         index = "Buzz"
    #     print(index)
        
            
    #     if index % 3 == 0:
    #        index = "Fizz"
    #     print(index)
        
    
          

    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here
    
    empty_dict = {}
    
    if not isinstance(sentence,str):
        raise ValueError("Enter string input")
        
    else:
        sentence = sentence.split()
        for word in sentence:
            word_length = len(word)
            
            empty_dict[word] = word_length
        print(empty_dict) 
        return empty_dict   
    
        

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here
    
def main():
    print(dog_years())
    
    num = int(input("Enter a number: \n"))
    print(fizzbuzz(num))
    
    sentence = input("Sentence:\n")
    print(word_lengths(sentence))
    
if __name__ == "__main__":
    main()