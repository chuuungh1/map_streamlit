import streamlit as st

st.write("카카오 지도와 장소 검색1")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>카카오 지도와 장소 검색</title>
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://code.jquery.com https://dapi.kakao.com 'unsafe-inline'; connect-src 'self' https://dapi.kakao.com; style-src 'self' 'unsafe-inline';">
    <style>
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

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript" src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=393132b4dfde1b54fc18b3bacc06eb3f&libraries=services"></script>

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
    function searchPlaces() {
        var keyword = document.getElementById('keyword').value; // 입력된 키워드 가져오기
        if (!keyword) {
            alert('키워드를 입력해주세요!');
            return;
        }

        var ps = new kakao.maps.services.Places(); // 장소 검색 객체 생성

        // 키워드로 장소 검색
        ps.keywordSearch(keyword, placesSearchCB);
    }

    // 장소 검색 결과 콜백 함수
    function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
            displayPlaces(data); // 장소 표시
        } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
            alert('검색 결과가 존재하지 않습니다.');
        } else if (status === kakao.maps.services.Status.ERROR) {
            alert('검색 중 오류가 발생했습니다.');
        }
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
        searchPlaces(); // 키워드로 장소 검색 호출
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
st.components.v1.html(html_code, height=800)  # height를 800으로 설정
