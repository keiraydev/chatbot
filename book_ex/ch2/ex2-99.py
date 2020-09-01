import matplotlib.pyplot as plt

# 데이터 정의
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# 바차트 출력
plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)
plt.yticks(sorted(temperatures))
plt.xlabel("season")
plt.ylabel("temperature")
plt.show()