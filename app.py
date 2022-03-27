import streamlit as st
import requests

# 各都道府県の人口
# 大正9年～平成27年 https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741&cycle_facet=tclass1&tclass2val=0
# 令和2年           https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001136464&cycle=0&tclass1=000001136466&tclass2val=0

st.title('日本の人口')

# https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&stat_infid=000032142402
response = requests.get('http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?appId=&lang=J&statsDataId=0003445099&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=')

with open('population2015.json', 'w') as f:
    for chunk in response.iter_content(100000):
        f.write(chunk)

