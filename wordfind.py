#Finds words that are in input file
def wordFind(inputfile,found): 
  with open(inputfile,'r') as file: #open file to be read
      linenum=1;
      foundnum=1;
      # read each line     
      for line in file: 
          # read each word       
          for word in line.split(): #for words in line
              # display the result            
              if(word == found): #match the word with user entered word.
                print(word," was found on line ",l)
                foundnum+=1
          linenum+=1 
      if(foundnum > 0):
         print(word," was not found")

