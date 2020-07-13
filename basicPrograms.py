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

  
