class Calc: # 사칙 연산 클래스
    def __init__(self, init_value):
        self.value = init_value
    def add(self, n):
        return self.value + n
    def sub(self, n):
        return self.value - n
    def mul(self, n):
        return self.value * n
    def div(self, n):
        return self.value / n


cal = Calc(100)
print("value = {0}".format(cal.value))
a = cal.add(100)
b = cal.sub(50)
c = cal.mul(2)
d = cal.div(2)
print("a={0}, b={1}, c={2}, d={3}".format(a, b, c, d))