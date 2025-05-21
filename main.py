# Solution for (1. Plus One)

# Writing a function that takes a list 
# of integers, converts the list of integers
# to a single integer, increments the single
# integer by 1, converts the result to list, 
# and returns the new list 

def plus_one(digits):
  # Convert list of integers to a single integer
  num = int(''.join(map(str, digits)))
  # Increment the single integer by 1
  num += 1
  # Convert the result to list
  result = [int(x) for x in str(num)]
  return result
# Display the result
print(plus_one([9]))


# Solution for (2. Alternate Min-Max Rearrangement)

# Writing a function that takes a list of integers
# and returns a new list with the elements rearranged
# such that the first element is the smallest, the second
# element is the largest, the third element is the second
# smallest, the fourth element is the second largest, and so on.

def min_max_rearrangement(list):
    # Sort the list
    list.sort()        
    # Initialize the result list
    print (list)
    result = []
    # Initialize the index for the smallest element
    i = 0
    # Initialize the index for the largest element
    j = len(list) - 1
    # Loop until all elements are added to the result list
    while i <= j:
        # Add the smallest element to the result list
        result.append(list[i])
        # Increment the index for the smallest element
        i += 1
        # Add the largest element to the result list
        result.append(list[j])
        # Decrement the index for the largest element
        j -= 1
    return result
# Display the result
print(min_max_rearrangement([3, 6, 9, -10, -5, -2, 0, 8]))