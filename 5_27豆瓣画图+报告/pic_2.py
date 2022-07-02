import pandas as pd
import re
import datetime
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from pyecharts.charts import Map
from pyecharts import options as opts
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



def plot_draw_pie(x,y, name):
    z = [i for i in range(len(x))]


    # 45为旋转的角度，不然x轴会特别密
    plt.xticks(rotation=45)

    # 绘制柱状图
    plt.figure(figsize=(50, 50))  # 定义坐标图尺寸
    plt.title(name, fontsize=50)
    plt.tick_params(labelsize=20) #坐标轴单位大小


    plt.pie(y,labels = x)  # 线型坐标点
    plt.rcParams.update({'font.size': 50})#增加右上角小图标
    plt.legend(loc=(1, 0.8))#右上角小图标大小

    save_name = './pic/' + name   # ⽂件名

    plt.savefig(save_name)
    print('over')
    plt.clf()



def plot_draw_zhifang_bar(yy,xx,name,tt):

    plt.figure(figsize=(150, 40))  # 定义坐标图尺寸

    #colors = ["#8dd3c7", "#bebada"]
    labels = tt
    z = [i for i in range(len(yy))]
    print(xx)
    print('^^^^^^^^^')
    plt.xticks(z, yy)
    plt.tick_params(labelsize=40)  # 坐标轴单位大小
    plt.hist(xx, bins=z,histtype="bar", rwidth=0.8,
             stacked=True, label=labels)
    plt.xlabel("国家", fontsize=50)
    plt.ylabel("数量", fontsize=50)
    plt.title(name, fontsize=50)
    plt.rcParams.update({'font.size': 20})
    plt.legend(labels=tt, loc='best')

    plt.savefig('./pic/' +name)
    plt.clf()


if __name__=='__main__':
    df = pd.read_excel("1.xlsx", sheet_name=0)
    title = df['标题']

    dir = df['导演: ']
    scip = df['编剧:']
    actor = df['主演: ']


    type = df['类型']
    country = df['制片国家/地区:']
    year = df[' 上映日期']
    long = df['片长: ']
    type = df['类型']
    wu = df['5星']
    si = df['4星']
    san = df['3星']
    er = df['2星']
    yi = df['1星']
    type_l = []
    for i in type:
        if isinstance(i, str):
            x = i.strip().split(' / ')
            type_l = type_l + x

    dic_type = {}
    for i in type_l:
        if i in dic_type:
            dic_type[i] += 1
        else:
            dic_type[i] = 1
    x = dic_type.keys()
    y = dic_type.values()
    name = '类型分布饼状图'
    plot_draw_pie(x,y,name)
    five = []
    for i in wu:
        if isinstance(i,str):
            five.append(float(i.strip().strip('%'))/100)
        else:
            five.append(i)
    four = []
    for i in si:
        if isinstance(i, str):
            four.append(float(i.strip().strip('%')) / 100)
        else:
            four.append(i)
    three = []
    for i in san:
        if isinstance(i, str):
            three.append(float(i.strip().strip('%')) / 100)
        else:
            three.append(i)
    two = []
    for i in er:
        if isinstance(i, str):
            two.append(float(i.strip().strip('%')) / 100)
        else:
            two.append(i)
    one = []


    for i in yi:
        if isinstance(i, str):
            one.append(float(i.strip().strip('%')) / 100)
        else:
            one.append(i)


    five = sum(five)
    four = sum(four)
    three = sum(three)
    two = sum(two)
    one = sum(one)
    y = [five,four,three,two,one]
    x = ['五星','四星','三星','二星','一星',]
    name ='评分分布'
    plot_draw_pie(x, y, name)



