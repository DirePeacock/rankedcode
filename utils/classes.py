"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary intervals 
to produce a list that has only mutually exclusive intervals.
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
          return "[" + str(self.start) + ", " + str(self.end) + "]"
    
    def print_interval(self):
        print(self.__str__(), end='')

    def __repr__(self):
        return f"<Interval object: {self.__str__()}>"

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()
