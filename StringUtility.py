class StringUtility:
  def __init__(self, string):
    self.string = string 


  '''
  this function is key for all the other methods to operate 
  args: (self)- needs to be used to call atributtes (string)- is being stored as an instance variable 
  return None
  '''

    
  def __str__(self):
    return self.string
    
  '''
  this function is used to return the string
  args: (self)- needs to be used to call atributtes
  return the string itself 
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
  this function counts the number of vowels in the string 
  args: (self)- needs to be used to call  
  return a string for anything more than 5 vowels or the number of vowels if less than 5
  '''


  def bothEnds(self):
    if len(self.string) <= 2:
      return ''
    return self.string [0:2] + self.string [-2:]

  '''
  this function takes first 2 and last 2 letters of the string and puts them together 
  args: (self)- needs to be used to call 
  return the first 2 and last 2 letters of the word
  '''

  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    
    return self.string[0]+self.string[1:].replace(self.string[0], '*')


  '''
  this function replaced a letter in the string with a star
  args: (self)- needs to be used to call  
  return a star replaced by a letter or if less than 1 then it returns the string itself 
  '''

  def asciiSum(self):
    
    return sum(map(ord,self.string))
  '''
  this function adds the ascii values of the string
  args: (self)- needs to be used to call 
  return the sum of ascii values thats in the string
  '''

  def cipher(self):
    space = ''
    for i in self.string:
      if i == ' ':
        y = ord(i)
      if i.islower():
        y = ord(i) + len(self.string)
        while y > ord('z'):
          y -=26
      elif i.isupper():
        y = ord(i) + len(self.string)
        while y > ord('Z'):
          y -=26

      space += chr(y)
    return space
      
  '''
  this function shifts characters within the string by the # of characters in the string itself.
  args: (self)- needs to be used to call 
  return the characters shifted by the length of the string
  '''


    