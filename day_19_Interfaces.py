class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        #Solution here -------------------->
        sum = n
        for i in range(1, n):
            if n % i == 0:
                sum = sum + i
        return sum
        #Solution here -------------------->



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)