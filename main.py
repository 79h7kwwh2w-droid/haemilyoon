import streamlit as st

st.title('영화 이건 꼭 보고 넘어가자(Title and star)')

if 'liked_movies' not in st.session_state:
    st.session_state.liked_moveis = set()

# 사용자 입력 받기
movie_property = st.selectbox{list(movie_data.keys(),key='feature_select')}

# 영화제목과 평점
movie_data = {
    '여운형': {
        'Aftersun': ' 4.2 ',
        'F1(2025)':'3.7',
        'Little Amelie or the Character of Rain(2025)':'4.1',
        'Escape(2024)':'3.4',
        'Ferrari(2023)':'3.2',
        'Joker(2019)':'3.8',
        'Marriage Story(2019)':'4.0',
        '기적(2021)':'3.7'
    },
    '해피엔딩': {
        'The Match(2025)':'3.4',
        'Wicked(2024)':'3.8',
        'The Intern(2015)':'3.3',
        'The Truman Show(1998)':'4.2',
        'The Notebook(2004)':'3.9'
     
    },
    '열린결말': {
        'Happyend(2024)':'4.0',
        'Decision to Leave':'4.0',
        'Nothing Serious':'3.2',
        'No Country for old Men(2007)':'4.3'
       
    },
    '불편한 엔딩': {
        'Michey 17(2025)':'3.6',
        'Super Happy Forever(2024)':'3.6',
        'The Girl with the Needle(2024)':'3.9',
        'Exhuma(2024)':'3.6',
        'Nobody Knows(2004)':'4.4'
    },
 
    '코미디': {
        'Good News(2025)' : '3.7',
        'Perhapes Love(2021)':'3.3',
        '스물(2015)':'3.2',
        '타짜(2006)':'3.8'
    },
    '뮤지컬스타일': {
        'La La Land' : '4.1',
        'tick, tick...BOOM!(2021)' : '3.8',
        'Begin Again(2013)':'3.5',
        'Whiplash(2014)':'4.4'
    },
     '잔잔한': {
        'Two Seasons, Two Strangers(2025)' : '3.6',
        'Little Forest(2018)':'4.0',
        '파수꾼(2010)':'3.9',
        'Love Letter(1995)':'4.1',
        '우리들(2016)':'4.0'
    }}

st.divider()

movies =movie_data[feature]

for title, star in movies.items():
    col1, col2 = st.columns([4,1])

with col1:
    st.write(f'🎬{title}⭐{star}')

with col2:
    if title in st.session_state.liked_movies:
        if st.button('💔찜 취소', key=f'unlike_{title}'):
           st.session_state.liked_movies,remove(title)
    else:
        if st.buttoen('❤️찜', key=f'like_{title}'):
            st.session_state.liked_movies,add(title)

st.driver()


st.subheader('❤️ 찜한 영화')

if st.sesion_state.liked_movies:
    for movie in st.session_state.liked_movies:
        st.write(f'{movie}')

else:
    st.write('✔️ 아직 찜한 영화가 없습니다.')
    


