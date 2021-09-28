def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    # This checks if a list of numbers is being passed into the function
    if isinstance(numbers, list):
        # Returns false for empty list
        # We take this out because it's covered in the if evens test
        # if numbers == []:
        #     return False
        # else:
        # if there is values in the list we set the number of evens to 0
        # then move to the for loop below
        # Change this for the list comprehension
        # evens = 0

        # list comprehension is great for refactoring

        # This would print whatever you called
        # print([n for n in numbers])

        # This prints 1 for every number in the list
        # print([1 for n in numbers])

        # this prints 1 for each even number and ignores the odds
        # print([1 for n in numbers if n % 2 == 0])

        # this sums the number of 1s
        # print(sum([1 for n in numbers if n % 2 == 0]))

        evens = sum([1 for n in numbers if n % 2 == 0])

        # THIS HAS BEEN REFINED ABOVE

        # for n in numbers:
        #     # Add up the even numbers
        # if n % 2 == 0:
        #     evens += 1

        # return True if evens isn't 0 and evens % 2==0 is false
        return True if evens and evens % 2 else False
        # THIS IS REFINED TOO

        # if evens:
        # if there are even values, we return if there is an even (True)
        # or uneven (False) amount of them
        # This is a truthy falsy
        # return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError("A list was not passed into the function")
    return None


if __name__ == "__main__":
    # remove the print statement to put it above
    print(even_number_of_evens(5))
