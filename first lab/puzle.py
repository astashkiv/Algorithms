class Puzle:

 comparisons = 0  
 swaps = 0


 @staticmethod
 def comperisons_method():
        Puzle.comparisons +=1
        return Puzle.comparisons

 @staticmethod
 def swap_method():
     Puzle.swaps += 1
     return Puzle.swaps

 def __init__(self, description, elements, width, height):
      self.description = description
      self.elements = elements
      self.width = width
      self.height = height

 def __str__(self):
   return "puzle: " + self.description + " elements: " + str(self.elements) + " width: " + str(self.width) + " height: " + str(self.height) 