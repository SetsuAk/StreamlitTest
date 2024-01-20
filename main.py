import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

# タイトル
st.title("Streamlit 超入門")

# テキストの追加
st.write("DataFrame")

# 表の追加
df = pd.DataFrame({
        "1列目": [1, 2, 3, 4],
        "2列目": [10, 20, 40, 30]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200) # 縦と横の大きさを調整できる
st.table(df) # staticな表を作ることができる


# マジックコマンド(markdown)
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# グラフを描く
chart_df = pd.DataFrame(
    np.random.rand(20, 3), 
    columns=["a", "b", "c"]
)
# 折れ線グラフ
st.line_chart(chart_df)
st.area_chart(chart_df)
st.bar_chart(chart_df)


# 地図へのmapping
map_df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], # 新宿付近の緯度・経度
    columns=["lat", "lon"]
)
# 地図も自動的に表示される
st.map(map_df)


st.write("Interactive Widgets")

# interactive(双方向)
if st.checkbox("Show Image"):
    # 画像の表示
    img = Image.open("sample1.png")
    st.image(img, caption="test", use_column_width=True)

option = st.selectbox(
    "あなたが好きな数字を教えてください。",
    options=list(range(1, 11))
)
st.write("あなたの好きな数字は",option,"です")

# text1 = st.text_input("あなたの趣味を教えてください。")
# サイドバーへの追加
# text1 = st.sidebar.text_input("あなたの趣味を教えてください。")
# st.write("あなたの趣味は",text1,"です")

# text2 = st.text_area("あなたの趣味を教えてください。")

# conditon = st.slider("あなたの今の調子は？", 0, 100, 50)
# サイドバーへの追加
# conditon = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# st.write("コンディション：",conditon)

# カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("左カラムでボタンを押しました。")


st.write("プログレスバーの表示")
"Start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)


# expander
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


