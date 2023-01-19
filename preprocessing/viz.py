import plotly.express as px
import matplotlib.pyplot as plt

def viz_data(data,features,title):
   
    plt.figure(1)
    data.plot(kind='line',x='ts_n',y= features,title = title)
    plt.show()
    


def viz_output(data,color,title):

    fig = px.scatter(data, x='ts_n', y='acc_x_n', color=color)
    fig.update_layout(title_text=title, title_x=0.5)
    fig.show()


def viz_bar(data,title):
    
    fig = px.bar(data.groupby(['label', 'cluster']).size().unstack(level=1))
    fig.update_layout(title_text=title, title_x=0.5)
    fig.show()
    