class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference =0
        

    # Add your code here -----> Solution 
    def computeDifference(self):
        self.maximumDifference = None
        total = []
        for i in range(len(self.__elements)):
            for j in range(i+1,len(self.__elements)):
                total.append(abs(self.__elements[i] - self.__elements[j]))
        total.sort(reverse =True)
        self.maximumDifference = total[0]
    # -----> Solution 


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)