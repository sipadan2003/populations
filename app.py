import streamlit as st
import requests
import pandas as pd
from pprint import pprint

# 各都道府県の人口
# 大正9年～平成27年 https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741&cycle_facet=tclass1&tclass2val=0
# 令和2年           https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001136464&cycle=0&tclass1=000001136466&tclass2val=0

st.title('日本の人口')

PREFS = {
    '全国',
    '北海道', '青森', '岩手', '宮城',   '秋田',
    '山形',   '福島', '茨城', '栃木',   '群馬',
    '埼玉',   '千葉'  '東京', '神奈川', '新潟',
    '富山',   '石川', '福井', '山梨',   '長野',
    '岐阜',   '静岡', '愛知', '三重',   '滋賀',
    '京都',   '大阪', '兵庫', '奈良',   '和歌山',
    '鳥取',   '島根', '岡山', '広島',   '山口',
    '徳島',   '香川', '愛媛', '高知',   '福岡',
    '佐賀',   '長崎', '熊本', '大分',   '宮崎',
    '鹿児島', '沖縄'
}

df = pd.read_csv('population/c01.csv')
df = df.drop('都道府県コード', axis=1)
df = df.drop('元号', axis=1)
df = df.drop('和暦（年）', axis=1)
df = df.drop('注', axis=1)
df = df.dropna(how='any')
pprint(df)

prefs = st.sidebar.multiselect(
        '都道府県名',
        PREFS,
        ['全国'],
        key=str
    )

