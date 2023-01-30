import requests
import pygal
from pygal.style import LightColorizedStyle as lcs,LightenStyle as ls

url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print("Status code:",r.status_code)
files=r.json()
a=files["items"]
names=[]
stars=[]
for x in a:
    names.append(x["name"])
    star={"value":x["stargazers_count"],"label":str(x["description"]),"xlink":x["html_url"]}
    stars.append(star)
my_style=ls("#333366",base_style=lcs)
my_config=pygal.Config()
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.width=1000
my_config.truncate_label=15
chart=pygal.Bar(my_config,style=my_style,x_label_rotation=45,show_legend=False,show_y_guides=False)
chart.title="Most-starred Python Projiects on Github"
chart.x_labels=names
chart.add("",stars)
chart.render_to_file("统计2.svg")