import plotly.express as px
import numpy as np
# 生成横轴数据
x = np.linspace(0, 2 * np.pi, 100)
# 生成正弦和余弦曲线数据
y_sin = np.sin(x)
y_cos = np.cos(x)
# 创建图表
fig = px.line(x=x, y=[y_sin, y_cos],
labels={'y': 'f(x)', 'x': 'x'})
# 修改图例
fig.data[0].name = 'Sine'
fig.data[1].name = 'Cosine'
# 显示图表
fig.show()
