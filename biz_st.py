import streamlit as st #streamlit 라이브러리 임포트 후 st라고 부를 것을 지정

# 타이틀 텍스트 출력

st.title("첫번째 웹 어플 만들기 👾")
"# 첫번째 웹 어플 만들기 👾"

# Streamlit Magic 기능으로 둘다 출력이 동일하게 됨

3.141592
[1234]

# 마크다운 문법

'''### Magic 적용
1. 숫자 후 한칸 띄기
2. 숫자 후 한칸 띄기
1. 앞에 숫자는 의미가 없음
  - 강조 : **강조**
  - 기울임 : *기울임*
   - 텍스트 입력

'''



"## 이건 부제목"


'''
#비즈니스 모델 분석 📗

사이트 연결하는 법

[네이버](https://www.naver.com)
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

```python

import streamlit as st

print("코드블럭")

```

'''

st.caption('')

with st.echo():
  #이 블럭의 코드와 결과 출력
  name='yull'
  st.write("Hello, Streamlit!",name)


st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"


import streamlit as st

'# 🎥: 이미지, 오디오, 동영상'

'#### :orange[이미지: st.image()]'
st.image(".//data//Pythonlogo.png", caption="파이썬 로고", width=500)

'#### :orange[오디오: st.audio()]'
st.audio(".//data//Shortmusic.mp3", format="audio/mpeg", loop=True)

'#### :orange[동영상: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open(".//data//Shortvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()

'# 📚: 콜아웃'

'#### :orange[정보: st.info()]'
st.info(
    icon="ℹ️",
    body='''
    **:sunglasses: 이것은 정보를 제공하는 콜아웃입니다.**
    - :red[빨간색 텍스트]
        - :blue[파란색 텍스트]
        - :green[초록색 텍스트]
        - :orange[주황색 텍스트]
    '''
)

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon="🚫")

'#### :orange[성공: st.success()]'
st.success('This is a success message', icon="✅")

'# :blue[데이터 테이블]'

'#### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
  {'id': [1,2,3], 
   'name':['Alice','Bob','Charlie'],
   'age':[23,24,25]}
)

df

'''
|이름|학번|학과|
|---|---|---| 
|홍길동|2023001|컴퓨터공학과|
|김철수|2023002|전자공학과|
|이영희|2023004|기계공학과|
'''

'### :orange[지표(Metric)]'
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", '70°F', '1.2°F')
col2.metric("Wind",'9 mph','-8%')
col3.metric("Humidity", '86%', "4%")
col4.metric('Pressure','1013 hPa','+12 hPa')

st.divider()
