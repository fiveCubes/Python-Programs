#leap year

def is_leap(year):
    leap = False

    if(year%4==0):
        if(year%100!=0):
          leap=True;
        elif(year%400 ==0):
          leap=True;

       
          
    
    # Write your logic here
    
    return leap

print(is_leap(1800))


#sub string efficient 
s='BAANANAS'
def minion_game(s):
  vowelPlayer=0;
  consPlayer=0;
  for i in range(len(s)):
    if s[i] in "AEIOU":
        vowelPlayer += (len(s)-i)
    else:
        consPlayer += (len(s)-i)
  
  if(vowelPlayer > consPlayer):
    print('Kevin',vowelPlayer)
  elif(vowelPlayer == consPlayer):
    print('Draw')
  else:
    print('Stuart',consPlayer)
    
  

minion_game(s)

# array manupulation

def arrayManipulation(n, queries):
    #print("running",n)
    
    master = [0]*(int(n)+2)
    for q in queries:
        start , end , value = q
        master[start] = master[start] + value
        master[end+1] = master[end+1] - value
        #print(master)
          #print('final',arr)
    #return max(arr)
    #sum=[]
    # initial=0
    max = x=0
    for k in master:
      x=x+k
      if(max < x):
        max=x
    return max


        
    #   sum.append(initial+master[x])
    #   initial=initial+master[x]
    # return (max(sum))
    
print(arrayManipulation(n,queries))

  
