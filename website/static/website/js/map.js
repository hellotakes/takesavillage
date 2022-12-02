window.addEventListener('load', function(){
    const map = initMap();
    addMarkersFromHtml(map);

})

function initMap(){
    const map = L.map('map').setView([50.8458, 4.352], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    return map;
}

function addMarkersFromHtml(map) {
    document.querySelectorAll(".map-marker").forEach(function (e) {
        addMarker(map, e.dataset.latitude, e.dataset.longitude);
    });
}

function addMarker(map, lat, long) {
    return L.marker([lat, long]).addTo(map);
}
