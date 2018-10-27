import sys


def number_is_bouncy(string_number):
    """
    This method will return if a number is bouncy.
    To check if a number is bouncy this method look in the index 1 to the end (string[1:]).
    The method check every iteration (number in the for) with the previous number to see if can find an increment or
    decrement sequence.
    If the string has both increment and decrement sequences the number is bouncy.
    :param string_number: String, Number to check. e.g. "155349"
    :return: Boolean, return if the number is bouncy or not. e.g. True or False.
    """
    has_increment, has_decrement = False, False
    for index, number in enumerate(str(string_number)):
        if index == 0:
            continue

        if number < string_number[index - 1]:
            has_decrement = True

        if number > string_number[index - 1]:
            has_increment = True

    if has_decrement and has_increment:
        return True
    return False


def find_bouncy_number_by_percentage(percentage_to_find, max_number):
    """
    Look for the first number that hit a percentage of bouncy numbers.
    e.g The first number that hit the 40% is 317 and the number that hit the 80% is 3816
    :param percentage_to_find: Float, percentage to find. e.g 80
    :param max_number: Integer, max number to check. e.g 90000000
    :return: 3 values.
        [Integer, Integer, Float] ->
            [Total numbers of bouncy found, First number that hit the percentage, Current percentage].
        e.g [3816, 4770, 80.0]
    """
    bouncy_counter = 0

    for n in range(100, max_number):
        if number_is_bouncy(str(n)):
            bouncy_counter += 1
            if (bouncy_counter / n) * 100 >= percentage_to_find:
                return bouncy_counter, n, (bouncy_counter / n) * 100


if __name__ == "__main__":
    """
    Description of the problem that the script is fixing
    
    If no digit in a number is exceeded by the digit to its left it’s called an increasing number – e.g. 134,468.
    
    Similarly if no digit is exceeded by the digit to its right it’s called a decreasing number – e.g. 66,420.
    
    We'll call a positive integer that is neither increasing nor decreasing a "bouncy" number – e.g. 155,349.
    """
    percentage_to_find = 0
    max_number = 0

    try:
        percentage_to_find = float(input("Write a percentage to find \n"))
        max_number = int(input("Write the max number (Default is 999999999999) \n")) or 999999999999
    except Exception as e:
        sys.exit("The values are incorrect. Percentage to find should be a float and Max number should be an integer")

    total_number_bouncy, number_hit_percentage, current_percentage = find_bouncy_number_by_percentage(
        percentage_to_find, int(max_number))

    print("Total numbers bouncy found: ", total_number_bouncy)
    print("First number that hit the percentage ({}) was: {}".format(percentage_to_find, number_hit_percentage))
    print("The current percentage was: ", current_percentage)

