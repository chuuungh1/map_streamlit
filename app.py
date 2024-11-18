import streamlit as st
import requests
import folium
from streamlit.components.v1 import html

# Kakao API 키
KAKAO_API_KEY = 'YOUR_KAKAO_API_KEY'

def search_places(keyword):
    url = f'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {'Authorization': f'KakaoAK {KAKAO_API_KEY}'}
    params = {'query': keyword, 'size': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('documents', [])
    return []

st.title("Kakao 지도 검색")

# 사용자로부터 키워드 입력 받기
keyword = st.text_input("키워드 입력:", "이태원 맛집")

if st.button("검색하기"):
    places = search_places(keyword)
    
    if places:
        # Folium 지도 생성
        map_center = [places[0]['y'], places[0]['x']]
        tile_map = folium.Map(location=map_center, zoom_start=15)

        # 마커 추가
        for place in places:
            folium.Marker(
                location=[place['y'], place['x']],
                popup=place['place_name'],
                icon=folium.Icon(color='blue')
            ).add_to(tile_map)

        # HTML로 변환
        map_html = tile_map.get_root().render()

        # Streamlit에서 HTML 표시
        html(map_html, height=500)
    else:
        st.warning("검색 결과가 없습니다.")
