import streamlit as st
import folium
import requests
from streamlit_folium import st_folium

# 카카오 API 키 설정 (여기에 발급받은 카카오 API 키를 입력하세요)
KAKAO_API_KEY = "393132b4dfde1b54fc18b3bacc06eb3f"  # 여기에 카카오 API 키를 입력


# 카카오맵 API를 사용하여 위치 검색
def search_location(query):
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {
        "Authorization": f"KakaoAK 6c1cbbc51f7ba2ed462ab5b62d3a3746"  # API 키를 헤더에 포함
    }
    params = {
        "query": query,  # 검색할 장소 이름
        "category_group_code": "SW8,FD6,CE7"  # 카테고리 코드 (예: 음식점, 카페 등)
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        documents = data.get("documents", [])
        if documents:
            return documents
        else:
            st.error("검색 결과가 없습니다.")
            return None
    else:
        st.error(f"API 요청 오류: {response.status_code}")
        return None


# 위치 검색 및 folium 지도 표시
def display_location_on_map():
    query = st.text_input("검색할 장소를 입력하세요:", "영남대역")  # 기본값: 영남대역
    if query:
        # 카카오 API로 장소 검색
        results = search_location(query)
        if results:
            # 지역 정보 추출
            locations = [(place["place_name"], place["address_name"], float(place["y"]), float(place["x"]))
                         for place in results]
            
            # 지역 이름 선택
            selected_place = st.selectbox("검색 결과를 선택하세요:", [name for name, _, _, _ in locations])

            # 선택된 장소의 정보 찾기
            for place in locations:
                if place[0] == selected_place:
                    name, address, latitude, longitude = place
                    st.write(f"장소 이름: {name}")
                    st.write(f"주소: {address}")

                    # folium 지도 생성
                    m = folium.Map(location=[latitude, longitude], zoom_start=17)
                    folium.Marker([latitude, longitude], popsup=f"{name}\n{address}",
                                  icon=folium.Icon(color='blue', icon='star')).add_to(m)

                    # Streamlit에서 folium 지도 표시
                    st_folium(m, width=725)


# Streamlit 앱 실행
st.title("카카오맵 위치 검색과 Folium 지도")

# 위치 검색 및 지도 표시
display_location_on_map()
