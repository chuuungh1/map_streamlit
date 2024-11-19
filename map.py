import streamlit as st

st.write("깃허브 + 스트림릿1")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>카카오 지도와 장소 검색</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="dapi.kakao.com/v2/maps/sdk.js?appkey=393132b4dfde1b54fc18b3bacc06eb3f&libraries=services"></script> <!-- 여기에 실제 API 키를 넣으세요 -->
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
        // 지도와 마커 관련 변수
        var map;
        var markers = [];

        // 카카오 지도 초기화
        function initMap() {
            var mapContainer = document.getElementById('map'),
                mapOption = {
                    center: new kakao.maps.LatLng(37.5665, 126.978), // 서울 시청
                    level: 3
                };

            map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성
        }

        // 장소 검색 함수
        function searchPlaces(lat, lon, radius, categoryCode) {
            var apiKey = "6c1cbbc51f7ba2ed462ab5b62d3a3746"; // Kakao Developers에서 발급받은 API 키
            var url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=" + categoryCode + "&x=" + lon + "&y=" + lat + "&radius=" + radius;

            $.ajax({
                method: "GET",
                url: url,
                headers: { Authorization: "KakaoAK " + apiKey },  // API 키 설정
                async: false // AJAX 요청이 여러 개일 경우 동기 방식으로 설정
            })
            .done(function (msg) {
                displayPlaces(msg.documents); // 장소 표시 함수 호출
            })
            .fail(function (jqXHR, textStatus, errorThrown) {
                console.error("API 호출 실패: " + textStatus, errorThrown);
            });
        }

        // 장소를 지도에 마커로 표시하는 함수
        function displayPlaces(places) {
            removeMarkers(); // 이전 마커 제거
            var placesList = $("#placesList");
            placesList.empty(); // 기존 목록 비우기

            for (var i = 0; i < places.length; i++) {
                var place = places[i];
                var position = new kakao.maps.LatLng(place.y, place.x);
                addMarker(position); // 마커 추가

                // 리스트에 장소 추가
                placesList.append("<li>" + place.place_name + " - " + place.address_name + "</li>");
            }
        }

        // 마커를 지도에 추가하는 함수
        function addMarker(position) {
            var marker = new kakao.maps.Marker({
                position: position
            });
            marker.setMap(map); // 지도 위에 마커를 표시합니다
            markers.push(marker); // 마커 배열에 추가
        }

        // 이전 마커 제거
        function removeMarkers() {
            for (var i = 0; i < markers.length; i++) {
                markers[i].setMap(null);
            }
            markers = []; // 마커 배열 초기화
        }

        // 버튼 클릭 시 장소 검색
        $("#searchButton").click(function() {
            // 예시 좌표 및 반경
            var lat = 37.5665; // 위도
            var lon = 126.978; // 경도
            var radius = 1000; // 반경 (미터)
            var categoryCode = "FD6"; // 음식점 카테고리 코드

            searchPlaces(lat, lon, radius, categoryCode); // 장소 검색 호출
        });

        // 페이지 로드 시 지도 초기화
        $(document).ready(function() {
            initMap(); // 지도 초기화
        });
    </script>
</body>
</html>

"""

# HTML 표시
st.components.v1.html(html_code, height=800)

