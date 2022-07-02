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

def max_plot_draw_bar(x,y,name):

    plt.figure(figsize=(120, 40))  # 定义坐标图尺寸
    plt.title(name, fontsize=50)

    # 45为旋转的角度，不然x轴会特别密
    plt.xticks(rotation=45)
    # 绘制柱状图
    z = [i for i in range(len(x))]
    plt.xticks(z, x)
    plt.tick_params(labelsize=50)  # 坐标轴单位大小
    for ii in y:
        plt.scatter(z,ii)
    savename = './pic/' + name
    plt.savefig(savename,  # province⽂件名：png、jpg、pdf
                dpi=100,  # 保存圖⽚像素密度
                facecolor='white',  # 視圖與邊界之間顏⾊設置
                edgecolor='lightgreen',  # 視圖邊界顏⾊設置
                bbox_inches='tight')  # 保存圖⽚完整
    print('over')
    plt.clf()


def plot_draw_bar(x,y,name):

    plt.figure(figsize=(120, 40))  # 定义坐标图尺寸
    plt.title(name, fontsize=50)

    # 45为旋转的角度，不然x轴会特别密
    plt.xticks(rotation=45)
    # 绘制柱状图
    z = [i for i in range(len(x))]
    plt.xticks(z, x)
    plt.tick_params(labelsize=50)  # 坐标轴单位大小
    plt.bar(z,y, width=0.7)
    savename = './pic/' + name
    plt.savefig(savename,  # province⽂件名：png、jpg、pdf
                dpi=100,  # 保存圖⽚像素密度
                facecolor='white',  # 視圖與邊界之間顏⾊設置
                edgecolor='lightgreen',  # 視圖邊界顏⾊設置
                bbox_inches='tight')  # 保存圖⽚完整
    print('over')
    plt.clf()


def plot_draw_plot(x,y, name):
    z = [i for i in range(len(x))]


    # 45为旋转的角度，不然x轴会特别密
    plt.xticks(rotation=45)

    # 绘制柱状图
    plt.figure(figsize=(90, 30))  # 定义坐标图尺寸
    plt.xticks(z, x)
    plt.tick_params(labelsize=50)  # 坐标轴单位大小
    plt.title(name, fontsize=50)
    plt.xlabel('time_2', fontsize=20)  # x坐標名称
    plt.ylabel('J', fontsize=20)  # y坐標名称
    plt.tick_params(labelsize=20) #坐标轴单位大小


    plt.plot(z, y)  # 线型坐标点
    plt.scatter(z, y,s=100,c='r')  # 线型坐标点

    save_name = './pic/' + name   # ⽂件名
    plt.savefig(save_name,  # ⽂件名：png、jpg、pdf
                dpi=100,  # 保存圖⽚像素密度
                facecolor='white',  # 視圖與邊界之間顏⾊設置
                edgecolor='lightgreen',  # 視圖邊界顏⾊設置
                bbox_inches='tight')  # 保存圖⽚完整
    print('over')
    plt.clf()


def plot_draw_pie(x,y, name):
    z = [i for i in range(len(x))]


    # 45为旋转的角度，不然x轴会特别密
    plt.xticks(rotation=45)

    # 绘制柱状图
    plt.figure(figsize=(50, 50))  # 定义坐标图尺寸
    plt.title(name, fontsize=50)
    plt.tick_params(labelsize=20) #坐标轴单位大小


    plt.pie(y,labels = x)  # 线型坐标点
    plt.rcParams.update({'font.size': 20})
    plt.legend(loc=(1, 0.8))

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

    type_l = []
    for i in type:
        if isinstance(i, str):
            x = i.strip().split(' / ')
            type_l = type_l + x

    t = list(set(type_l))
    i = [0 for i in range(len(t))]
    zero_type = dict(zip(t, i))
    print(zero_type)
    #year = [re.sub('/.','',i) for i in year]
    year_l = []
    for j,i in enumerate(year):
        if isinstance(i, datetime.date):
            year_l.append(i.year)
        else:
            year_l.append(i)
    year_l.sort()
    dic_year = {}
    for i in year_l:
        if i in dic_year:
            dic_year[i] += 1
        else:
            dic_year[i] = 1

    xx = dic_year.keys()
    y = dic_year.values()
    name = '年份分布'
    plot_draw_plot(xx,y, name)#年份分布图
    type_l
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

    # dic_type_year = {}
    # for j in xx:
    #     dic_type_year[j] = zero_type.copy()
    #
    # for i,j in enumerate(year_l):
    #     x = type[i].strip().split(' / ')
    #     for z in x:
    #         dic_type_year[j][z] +=1
    # ty_year_lis = []
    # for ii in xx:
    #     temp = []
    #     for i in t:
    #         temp.append(dic_type_year[ii][i])
    #     print(temp)
    #     ty_year_lis.append(temp)
    # name = '类型点状分布'
    # print(xx)
    # xx = list(xx)
    #
    # plot_draw_zhifang_bar_2(xx, ty_year_lis, name,t)


    long_l = []
    for i in long:
        if isinstance(i, str):
            x = int(i.replace('分钟', ''))
            long_l.append(x)
        else:
            long_l.append(int(x))
    long_l.sort()
    long = []
    for i in long_l:
        long.append(i//10*10)
    print(long)
    # df['导演:']
    dic_long = {}
    for i in long:
        if i in dic_long:
            dic_long[i] += 1
        else:
            dic_long[i] = 1

    x = dic_long.keys()
    y = dic_long.values()
    name = '时间段分布'
    plot_draw_bar(x,y, name)#时间时段分布图

    dir = df['导演: ']
    scip = df['编剧:']
    actor = df['主演: ']


    dic_country = {}
    country_l = []
    for i in country:
        if isinstance(i, str):
            x = i.strip().split(' / ')
            country_l = country_l + x

    for i in country_l:
        if i in dic_country:
            dic_country[i] += 1
        else:
            dic_country[i] = 1
    x = dic_country.keys()
    y = dic_country.values()
    name = '国家'


    dic_dic = {}
    for i in country_l:
        dic_dic[i] = zero_type.copy()
    print(']]]]',zero_type)
    for j,i in enumerate(country):
        i = i.strip().split(' / ')
        for z in i:
            t_j = type[j].strip().split(' / ')
            for ii in t_j:
                if ii in dic_dic[z]:
                    dic_dic[z][ii] +=1

    print('******',dic_dic)
    ty_co_lis = []
    country_l = list(dic_country.keys())

    print('+++++',country_l,'++++++')
    print('------', t, '++++++')
    print(dic_dic['中国香港']['历史'])
    for ty in t:
        temp = []

        for jjj in range(len(country_l)):
            x = country_l[jjj]
            z = dic_dic[x][ty]
            temp.append(z)
        print(temp)
        ty_co_lis.append(temp)

    name = '直方'
    plot_draw_zhifang_bar(country_l,ty_co_lis, name,t)


