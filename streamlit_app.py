import streamlit as st
#from IPython.display import Image
import openai

openai.api_key = "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"

#タイトル作成
st.title("😱 絵日記")

# テキスト入力フォームを作成
text_input1 = st.text_input("絵にしたいテキストを入力してください")

# テキスト入力フォームを作成
text_input2 = st.text_input("絵日記の設定を作成して下さい")

# ボタンを作成
if st.button("絵日記生成"):
    if text_input1:
        response = openai.Image.create(
            prompt=text_input1+"anime-sytle",
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']

        # URLから直接画像を読み込む
        st.image(image_url)

    if text_input2:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a diary based on the following story in Japanese. {text_input2}"},
        ]
    )
        # 結果の表示
        st.write(response['choices'][0]['message']['content'])
