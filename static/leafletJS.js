var mymap = L.map('mapid').setView([1.3521, 103.8198], 9);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiamFhYmJlcndvY2t5IiwiYSI6ImNqamN0YTFxazBsYTMzd2xrYzB1YTA2dXAifQ.VJmG7SLHGEti2kkG-68Y2A'
}).addTo(mymap);