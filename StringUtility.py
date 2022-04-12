class StringUtility:
  def __init__(self, string):
    self.string = string 


  '''
  this function
  args: (self)-  (string)-
  return None
  '''

    
  def __str__(self):
    return self.string
    
  '''
  this function
  args: (self)- 
  return None
  '''
  
  def vowels(self):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count= 0
    for letter in self.string:
      if letter in vowel:
        count += 1
    if count < 5:
      return str(count)
    else:
      return "many"

  '''
  this function
  args: (self)-  
  return a string for anything more than 5 vowels or the number of vowels if less than 5
  '''


  def bothEnds(self):
    if len(self.string) <= 2:
      return ''
    return self.string [0:2] + self.string [-2:]

  '''
  this function
  args: (self)- 
  return the first 2 and last 2 letters of the word
  '''

  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    
    return self.string[0]+self.string[1:].replace(self.string[0], '*')


  '''
  this function
  args: (self)-  
  return a star replaced by a letter or if less than 1 then it returns the string itself 
  '''

  def asciiSum(self):
    return sum(map(ord,self.string))
  '''
  this function
  args: (self)-  
  return the sum of ascii values thats in the string
  '''

  def cipher(self):
    pass



    