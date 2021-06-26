# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objs as go
import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

# person = {
#     'first_name': 'Nohossat',
#     'last_name' : 'TRAORE',
#     'address' : '9 rue Léon Giraud · PARIS · FRANCE',
#     'job': 'Web developer',
#     'tel': '0678282923',
#     'email': 'nohossat.tra@yahoo.com',
#     'description' : 'Suite à une expérience internationale en développement web et dans le domaine des arts, l’impact de l’intelligence artificielle dans nos vies me surprend de jour en jour. \n Aujourd’hui, je souhaite changer de cap et comprendre les secrets que recèlent nos données. J’aimerais mettre à profit ces découvertes au service des entreprises/associations à dimension sociale.',
#     'social_media' : [
#         {
#             'link': 'https://www.facebook.com/nono',
#             'icon' : 'fa-facebook-f'
#         },
#         {
#             'link': 'https://github.com/nono',
#             'icon' : 'fa-github'
#         },
#         {
#             'link': 'linkedin.com/in/nono',
#             'icon' : 'fa-linkedin-in'
#         },
#         {
#             'link': 'https://twitter.com/nono',
#             'icon' : 'fa-twitter'
#         }
#     ],
#     'img': 'img/img_nono.jpg',
#     'experiences' : [
#         {
#             'title' : 'Web Developer',
#             'company': 'AZULIK',
#             'description' : 'Project manager and lead developer for several AZULIK websites.',
#             'timeframe' : 'July 2018 - November 2019'
#         },
#         {
#             'title' : 'Freelance Web Developer',
#             'company': 'Independant',
#             'description' : 'Create Wordpress websites for small and medium companies. ',
#             'timeframe' : 'February 2017 - Present'
#         },
#         {
#             'title' : 'Sharepoint Intern',
#             'company': 'ALTEN',
#             'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
#             'timeframe' : 'October 2015 - October 2016'
#         }
#     ],
#     'education' : [
#         {
#             'university': 'Paris Diderot',
#             'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
#             'description' : 'Gestion de projets IT, Audit, Programmation',
#             'mention' : 'Bien',
#             'timeframe' : '2015 - 2016'
#         },
#         {
#             'university': 'Paris Dauphine',
#             'degree': 'Master en Management global',
#             'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
#             'mention' : 'Bien',
#             'timeframe' : '2015'
#         },
#         {
#             'university': 'Lycée Turgot - Paris Sorbonne',
#             'degree': 'CPGE Economie & Gestion',
#             'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
#             'mention' : 'N/A',
#             'timeframe' : '2010 - 2012'
#         }
#     ],
#     'programming_languages' : {
#         'HMTL' : ['fa-html5', '100'], 
#         'CSS' : ['fa-css3-alt', '100'], 
#         'SASS' : ['fa-sass', '90'], 
#         'JS' : ['fa-js-square', '90'],
#         'Wordpress' : ['fa-wordpress', '80'],
#         'Python': ['fa-python', '70'],
#         'Mongo DB' : ['fa-database', '60'],
#         'MySQL' : ['fa-database', '60'],
#         'NodeJS' : ['fa-node-js', '50']
#     },
#     'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
#     'interests' : ['Dance', 'Travel', 'Languages']
# }

person = {
    'summary':'Summary简介',
    'sytext':'我是一个学生，有良好的心理素质，能正确的认识和评价自己，虚心接受他人的建议。拥有良好表达和沟通能力，性情温和，易于他人合作，形成融洽的合作关系。积极进取、注意细节、工作态度认真、责任心强、并有很强的团队合作精神与合作能力、注重工作效率、时间观念强，有上进心，知错改错。',
    'rows':[
        {
            'p1':'姓名：张质量',
            'p2':'地址：中国湖北',
            'p3':'电话：451289200124521',
        },
        {
            'p1':'HTML',
            'p2':'CSS (Stylus)',
            'p3':'python',
        },
        {
            'p1':'C',
            'p2':'mysql',
            'p3':'android app',
        },
        {
            'p1':'Java',
            'p2':'java Web',
            'p3':'JavaScript',
        }
    ],
    'experiences':[
        {
            'time':'2020-12-5',
            'experience':'在login页面进行输入用户名和密码进行登录，同时也有一个注册的按钮，点击即可进行注册，注册的页面，即ZhuCe.jsp的模样和login.jsp差不多，还有数据库文件，通过用户名和密码进行注册的，还有登录成功loginSuccess.jsp、注册成功index.jsp的页面，可以在页面上写上登录成功、注册成功四个字，代表我们的登录和注册已经成功了。'
        },
        {
            'time':'2021-1-20',
            'experience':'用python进行数据分析,许许多多的人（包括我自己）都很容易爱上Python这们语言。自从1991年诞生以来，Python现在已经成为最受欢迎的动态编程语言之一，其他还有Perl、Ruby等。由于拥有大量的Web框架（比如Rails（Ruby）和Django（Python）），自从2005年，使用Python和Ruby进行网站建设工作非常流行。这些语言常被称作脚本（scripting）语言，因为它们可以用于编写简短而粗糙的小程序（也就是脚本）。'
        }
    ]
}
@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)





@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))
   
@app.route('/chart')
def chart():
    return render_template('chartsajax.html',graphJSON=gm(),graphJSON1=gm1()
        ,graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5())

def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())
    fig = px.line(df[df['country']==country], x="year", y="gdpPercap")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm1():
    df = pd.DataFrame(px.data.gapminder())
    fig1 = px.area(df, x="year", y="gdpPercap",color="continent",line_group="country")
    graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def gm2():
    df = pd.DataFrame(px.data.gapminder())
    fig2 = px.scatter(
  df   # 绘图使用的数据
  ,x="gdpPercap" # 横纵坐标使用的数据
  ,y="lifeExp"  # 纵坐标数据
  ,color="continent"  # 区分颜色的属性
  ,size="pop"   # 区分圆的大小
  ,size_max=60  # 圆的最大值
  ,hover_name="country"  # 图中可视化最上面的名字
  ,animation_frame="year"  # 横轴滚动栏的属性year
  ,animation_group="country"  # 标注的分组
  ,facet_col="continent"   # 按照国家country属性进行分格显示
  ,log_x=True  # 横坐标表取对数
  ,range_x=[100,100000]  # 横轴取值范围
  ,range_y=[25,90]  # 纵轴范围
  ,labels=dict(pop="Populations",  # 属性名字的变化，更直观
               gdpPercap="GDP per Capital",
               lifeExp="Life Expectancy")
    )
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2

def gm3():
    df = pd.DataFrame(px.data.gapminder())
    fig3 = fig = px.scatter_geo(
  df,   # 数据
  locations="iso_alpha",  # 配合颜色color显示
  color="continent", # 颜色
  hover_name="country", # 悬停数据
  size="pop",  # 大小
  animation_frame="year",  # 数据帧的选择
  projection="natural earth"  # 全球地图
                    )
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3

def gm4():
    df = pd.DataFrame(px.data.gapminder())
    fig4 = px.choropleth(
  df,  # 数据集
  locations="iso_alpha",  # 配合颜色color显示
  color="lifeExp", # 颜色的字段选择
  hover_name="country",  # 悬停字段名字
  animation_frame="year",  # 注释
  color_continuous_scale=px.colors.sequential.Plasma,  # 颜色变化
  projection="natural earth"  # 全球地图
             )
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4

def gm5():
    df = pd.DataFrame(px.data.gapminder())
    fig5 = px.choropleth(
  df,  # 数据集
  locations="iso_alpha",  # 配合颜色color显示
  color="gdpPercap", # 颜色的字段选择
  hover_name="country",  # 悬停字段名字
  animation_frame="year",  # 注释
  color_continuous_scale=px.colors.sequential.Plasma,  # 颜色变化
  projection="orthographic"  # 球形地图
             )
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5

@app.route('/titanic')
def tita():
    return render_template('titanic.html',graphJSON6=gm6(),graphJSON7=gm7()
        ,graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10(),graphJSON11=gm11())

def gm6():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    labels = ['survived','death']
    df1=df['survived']==1
    df2=df['survived']==0
    values = [df1.sum(),df2.sum()]
    trace = [go.Pie(
        labels = labels, 
        values = values, 
        hole =  0.1,
        hoverinfo = "label + percent")]
    layout = go.Layout(
        title = '泰坦尼克号生存饼环图'
    )
    fig = go.Figure(data = trace, layout = layout)
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6

def gm7():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    fig1 = px.histogram(df,x="age",y="survived",color="sex",barmode="group")
    graphJSON7 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON7

def gm8():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    df.loc[df["survived"] == 0, "survived"] = 2
    fig2 = px.bar(
  df,  # 数据集
  x="sex",  # 横轴
  y="survived",  # 纵轴
  color="sex",  # 颜色参数取值
  barmode="group",  # 柱状图模式取值
  facet_col="survived",  # 列元素取值  
    )
    graphJSON8 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON8

def gm9():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    labels = ['mam','woman']
    df1=df['sex']=="male"
    df2=df['sex']=="female"
    values = [df1.sum(),df2.sum()]
    trace = [go.Pie(
        labels = labels, 
        values = values, 
        hoverinfo = "label + percent")]
    layout = go.Layout(
        title = '泰坦尼克号男女饼图'
    )
    fig3 = go.Figure(data = trace, layout = layout)
    graphJSON9 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON9

def gm10():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    labels = ['first_class','second_class','thrid_class']
    df1=df['pclass']==1
    df2=df['pclass']==2
    df3=df['pclass']==3
    values = [df1.sum(),df2.sum(),df3.sum()]
    trace = [go.Pie(
        labels = labels, 
        values = values, 
        hoverinfo = "label + percent")]
    layout = go.Layout(
        title = '泰坦尼克号各阶级人数饼图'
    )
    fig4 = go.Figure(data = trace, layout = layout)
    graphJSON10 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON10

def gm11():
    data = pd.read_csv("titanic.csv")
    df = pd.DataFrame(data)
    df["age"] = df["age"].fillna(df["age"].median())
    fig5=px.scatter(
    df,  # 数据集
    x="pclass",  # 横坐标值
    y="age",  # 纵坐标取值
    color="sex",  # 颜色
    size="age"
    )
    graphJSON11 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON11


@app.route('/senti')
def main():
    text = ""
    values = {"positive": 0, "negative": 0, "neutral": 0}

    with open('ask_politics.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(reader):
            if idx > 0 and idx % 2000 == 0:
                break
            if  'text' in row:
                nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
                text = nolinkstext

            blob = TextBlob(text)
            for sentence in blob.sentences:
                sentiment_value = sentence.sentiment.polarity
                if sentiment_value >= -0.1 and sentiment_value <= 0.1:
                    values['neutral'] += 1
                elif sentiment_value < 0:
                    values['negative'] += 1
                elif sentiment_value > 0:
                    values['positive'] += 1

    values = sorted(values.items(), key=operator.itemgetter(1))
    top_ten = list(reversed(values))
    if len(top_ten) >= 11:
        top_ten = top_ten[1:11]
    else :
        top_ten = top_ten[0:len(top_ten)]

    top_ten_list_vals = []
    top_ten_list_labels = []
    for language in top_ten:
        top_ten_list_vals.append(language[1])
        top_ten_list_labels.append(language[0])

    graph_values = [{
                    'labels': top_ten_list_labels,
                    'values': top_ten_list_vals,
                    'type': 'pie',
                    'insidetextfont': {'color': '#FFFFFF',
                                        'size': '14',
                                        },
                    'textfont': {'color': '#FFFFFF',
                                        'size': '14',
                                },
                    }]

    layout = {'title': '<b>意见挖掘</b>'}

    return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
