def insertion_sort(items):
    # Split the list into sorted and unsorted
    # For each element in unsorted...
    counter = 0
    for i in range(1, len(items)):
        print(items)
        # Insert that element into the correct place in sorted by:
        # Store the element in a temp variable
        temp = items[i]
        # Shifting all larger sorted elements to the right by 1
        j = i
        while j > 0 and temp < items[j - 1]:
            counter += 1
            items[j] = items[j - 1]
            j -= 1
        # Insert the element after the first smaller elememnt
        items[j] = temp
        print(f"counter: {counter}")
    return items


# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
      smallest_index = i

      for j in range(i, len(arr)):
        if arr[j] < arr[smallest_index]:
          smallest_index = j
      
      arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


def bubble_sort(arr):
  swapped = False
  
  for _ in arr:
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swapped = True

    if not swapped:
      break
      
  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr