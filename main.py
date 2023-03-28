def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
  return sorted(arr)

"""
How does this solution ensure data immutability?
  By creating the array inside the function there is no data changed outside the function.

Is this solution a pure function? Why or why not?
  Yes, the input value stays the same and there are no varibales outside of the function       changed.

Is this solution a higher order function? Why or why not?
  Yes, the function using sorted() in the return statement is an example of a higher order     function.

Would it have been easier to solve this problem using a different programming style?
  Probably, but that wasn't the assignment.

Why in particular is functional programming a helpful paradigm when solving this problem?
  Because it takes less space than OOP would solving the same problem but has better           readability than a lambda function.
"""
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
  def repair(self):
    self.condition = "repaired"

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation - If the classes for the pods were just other objects it would probably do this better
Abstraction - Not too much flexibility on the second and third classes but a decent amount on the first
Inheritance - There is inheritence if you consider init
Polymorphism - Not sure how this is much different then the second and third pillars

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
It might have been easier but not stuck to DRY method as well

How in particular did Object Oriented Programming assist in the solving of this problem?
By using the podracer class to create two other classes
"""