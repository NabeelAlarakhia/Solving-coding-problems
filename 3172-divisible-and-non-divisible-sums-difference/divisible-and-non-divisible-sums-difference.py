class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        notDivisible = set()
        Divisible = set()
        total = range(1,n+1)
        for i in total:
            if i % m != 0:
                notDivisible.add(i)
            else:
                Divisible.add(i)
        num1 = sum(notDivisible)
        num2 = sum(Divisible)
        return num1 - num2
            