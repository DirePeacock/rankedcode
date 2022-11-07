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

class Solution():
    @staticmethod
    def solution(intervals, new_interval):

        # sorted
        # intervals.sort(key=lambda ntrvl: ntrvl.start)
        mergedIntervals = []
        
        #iterate thru the rest
        for i in range(len(intervals)-1): 
            j=i+1
            
            
            
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                mergedIntervals.append(Interval(start,end))
                start = interval.start
                end = interval.end
        
        mergedIntervals.append(Interval(start,end))
        return mergedIntervals


        


cases = [([1,4],[2,5],[7,9]),
         ([6,7],[2,4],[5,9]),
         ([1,4],[2,6],[3,5])]

def main():
    for case in cases:
        print(f'{case}\n')
        retval = Solution.solution(list(Interval(*interval) for interval in case))
        print(f"{case}\n=\t{str(retval)}\n")
if __name__=="__main__":
    main()