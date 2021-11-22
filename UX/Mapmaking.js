  function makemap(mymap){


  L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
  }).addTo(mymap);

  //Lägger till två markers som ger en popup när man klickar på dem
  var marker1= L.marker([63.8250972,20.3109672]).addTo(mymap);
  var marker2= L.marker([63.8263093156, 20.3110416520]).addTo(mymap);
  var marker3= L.marker([63.8283182582, 20.3143416167]).addTo(mymap);
  var marker5= L.marker([63.8325499652, 20.3168760740]).addTo(mymap);
  var marker6= L.marker([63.8360593,20.3163476]).addTo(mymap);

  marker1.bindPopup("<a href=#>Sensor 1</a>").openPopup();
  marker6.bindPopup("<a href=sensor6.html>Sensor6</a>").openPopup();
}
