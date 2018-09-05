import matplotlib
from matplotlib import pyplot as plt

# 显示中文
matplotlib.rcParams["font.sans-serif"] = ["simhei"]
matplotlib.rcParams["font.family"] = "sans-serif"

# plt.plot([1,2], [3,4], '--', color='r',label='linel')
# plt.xlabel('X轴')
# plt.ylabel('Y轴')
# plt.legend() #绘制
# plt.show() #显示

# 柱状图
# left, 位置x轴
# height, y轴
# width=0.8 柱子的大小
plt.bar([1], [122], label="qwe")
plt.bar([3], [43], label='asd')
plt.bar([5], [543], label="zxc")
plt.legend()
plt.show()