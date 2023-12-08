import matplotlib.pyplot as plt

# 核心设计的参数
core_designs = ['HW3BigCore', 'HW3LittleCore', 'HW3MediumCore1', 'HW3MediumCore2', 'HW3MediumCore3', 'HW3MediumCore4']

# 成本和能数据
costs = [15752, 2456, 4456, 3456, 6392, 7124]
performances = [0.611809, 0.475635, 0.477614, 0.558684, 0.486200, 0.593515]

# 创建帕累托前沿图
plt.figure(figsize=(10, 6))
plt.scatter(performances, costs, s=100, c='blue', marker='o')

# 添加标签
for i, core in enumerate(core_designs):
    plt.annotate(core, (performances[i], costs[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# 添加坐标轴标签
plt.xlabel('(Performance)')
plt.ylabel('(Cost)')

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()