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
        if numbers == []:
            return False
        else:
            # if there is values in the list we set the number of evens to 0
            # then move to the for loop below
            evens = 0

        for n in numbers:
            # Add up the even numbers
            if n % 2 == 0:
                evens += 1
        if evens:
            # if there are even values, we return if there is an even (True) or uneven (False) amount of them
            # This is a truthy falsy
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")
    return None


if __name__ == "__main__":
    print(even_number_of_evens(5))
