
import streamlit as st

st.write("깃허브 + 스트림릿")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>카카오 지도와 장소 검색</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=393132b4dfde1b54fc18b3bacc06eb3f&libraries=services" async defer></script>
    <style>
        #map { width: 100%; height: 500px; }
        #placesList { list-style: none; padding: 0; }
        #placesList li { margin: 5px 0; }
    </style>
</head>
<body>
    <h1>카카오 지도와 장소 검색</h1>
    <input type="text" id="keyword" placeholder="검색할 장소 입력" />
    <button id="searchButton">장소 검색</button>
    <ul id="placesList"></ul>
    <div id="map"></div>

    <script>
        // SDK 로드를 기다리는 함수
        function initMap() {
            if (typeof kakao !== 'undefined' && kakao.maps) {
                var map = new kakao.maps.Map(document.getElementById('map'), {
                    center: new kakao.maps.LatLng(37.5665, 126.978),
                    level: 3
                });
            } else {
                console.log("Kakao Maps SDK not loaded yet");
            }
        }

        // SDK 로드 후 실행
        window.onload = function() {
            var checkKakaoLoaded = setInterval(function() {
                if (typeof kakao !== 'undefined' && kakao.maps) {
                    clearInterval(checkKakaoLoaded);
                    initMap();
                }
            }, 100);
        };
    </script>
</body>
</html>
"""

# HTML 표시
st.components.v1.html(html_code, height=800)
