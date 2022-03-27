import streamlit as st
import pandas as pd
import altair as alt
from pprint import pprint

# 各都道府県の人口
# 大正9年～平成27年 https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001011777&cycle=0&tclass1=000001094741&cycle_facet=tclass1&tclass2val=0
# 令和2年           https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001136464&cycle=0&tclass1=000001136466&tclass2val=0

# https://altair-viz.github.io/gallery/bar_chart_with_labels.html#gallery-bar-chart-with-labels
# https://altair-viz.github.io/gallery/index.html
# https://qiita.com/keisuke-ota/items/80d64153c499c8cc4774#%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0-histgram
# https://qiita.com/keisuke-ota/items/aa93f45b3a9fc520541d#%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0
# https://altair-viz.github.io/user_guide/encoding.html

st.title('日本の人口')

PREFS = {
    '全国',
    '北海道', '青森県', '岩手県', '宮城県',   '秋田県',
    '山形県', '福島県', '茨城県', '栃木県',   '群馬県',
    '埼玉県', '千葉県',  '東京都', '神奈川県', '新潟県',
    '富山県', '石川県', '福井県', '山梨県',   '長野県',
    '岐阜県', '静岡県', '愛知県', '三重県',   '滋賀県',
    '京都府', '大阪府', '兵庫県', '奈良県',   '和歌山県',
    '鳥取県', '島根県', '岡山県', '広島県',   '山口県',
    '徳島県', '香川県', '愛媛県', '高知県',   '福岡県',
    '佐賀県', '長崎県', '熊本県', '大分県',   '宮崎県',
    '鹿児島県', '沖縄県'
}


df = pd.read_csv('./population/c01.csv')

def manufactureData(df):
    df = df.drop('都道府県コード', axis=1)
    df = df.drop('元号', axis=1)
    df = df.drop('和暦（年）', axis=1)
    df = df.drop('人口（男）', axis=1)
    df = df.drop('人口（女）', axis=1)
    df = df.drop('注', axis=1)
    df = df.dropna(how='any')
    df = df.rename(
        columns={'都道府県名':'都道府県', '西暦（年）':'年', '人口（総数）': '人口'}
    )
    df['年'] = df['年'].astype(int)
    return df

df = manufactureData(df)

prefs = st.sidebar.multiselect(
    '都道府県',
    PREFS,
    ['東京都'],
    key=str
)

ymin, ymax = st.sidebar.slider(
    '人口の範囲',
    0, 150_000_000, (0, 14_000_000), step=10_000
)

def concatDataFrames(allDf, pref, df):
    #    df1 = df[df.都道府県 == "北海道"]
    #    df2 = df[df.都道府県 == "青森県"]
    #    df3 = df[df.都道府県 == "沖縄県"]
    df2 = allDf[allDf.都道府県 == pref]
    print(df2)
    return pd.concat([df, df2])

data = pd.DataFrame()
for p in prefs:
    data = concatDataFrames(df, p, data)

print(data)

chart = alt.Chart(data).mark_line().encode(
    y=alt.Y("人口:Q", scale=alt.Scale(domain=[ymin, ymax])),
#    y=alt.Y("人口:Q"),
    x=alt.X('年:O'),
    color='都道府県:N'
)
st.altair_chart(chart, use_container_width=True)
