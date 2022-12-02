window.addEventListener('load', function(){
    const map = initMap();

})

function initMap(){
    var map = L.map('map').setView([50.8458, 4.352], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    return map;
}

function addMarker(map, lat, long) {
    return L.marker([50.847233, 4.348794]).addTo(map);
}
