a =[1,3,4,5,7,8,9,10]

def binarySearch(lst, value):
  start_idx = 0
  end_idx= len(lst)

  while(start_idx < end_idx):
    mid_idx = (start_idx + end_idx)//2
    mid_value = lst[mid_idx]

    if(mid_value == value):
      return mid_idx
    
    if(mid_value < value):
      start_idx = mid_idx +1 
    
    if(mid_value > value):
      end_idx = mid_idx
    
  return "not found"


print(binarySearch(a,5))
