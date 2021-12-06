/* Functions used for map making --------------------------------------- */

/* Funciton to create base map */
function makeMap(){
    map = L.map("utbredning").setView([63.834219,20.315930], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
    }).addTo(map);

    /* Loop to add all installed sensors to the current map
    * Code has to be moved to .html so the queryset can be added
    */

    /*
    var x_cord;
    var y_cord;

    {% for dataEntry in sensor_objects %}
    // Get coordinates from the database
    x_cord = dataEntry.x_cord
    y_cord = dataEntry.y_cord

    /* Add markers to the map
    L.marker([x_cord,y_cord]).addTo(mymap);

    {% endfor %}
    */


    /* Manual way to add markers to map
    * Should be depreciated but coordinates are in SWEREF 99
    * in the database so we cannot use the at the moment
    */
    var marker1= L.marker([63.8250972,20.3109672]).addTo(map);
    var marker2= L.marker([63.8263093156, 20.3110416520]).addTo(map);
    var marker3= L.marker([63.8283182582, 20.3143416167]).addTo(map);
    var marker5= L.marker([63.8325499652, 20.3168760740]).addTo(map);
    var marker6= L.marker([63.8360593,20.3163476]).addTo(map);

}

/* Function to update map after the sensor in dropdown is changed */
function loadImage() {
    /* Get the chosen value in the dropdown menu */
    var sensorToLook = getSelectedSensor();
    var simlationHeight = getSelectedHeight();

    /* Set path to image of simulation */
    var imgPath = 'static/Simulations/'+sensorToLook+'_waterlevel_'+simlationHeight+'.PNG'

    /* Set the image bounds of the added image */
    var cornerUL = L.latLng(63.840277,20.290099)
    var cornerLR = L.latLng(63.816073,20.336459)
    var imageBounds = L.latLngBounds(cornerUL, cornerLR);

    /* remove image layer if it already exists.
     * Then add a new simulation based on the value
     * in the sensor dropdown menu
     */
    if (map.hasLayer(image)) {
        map.removeLayer(image);
        console.log('Removed image and added new')
        imageNew = L.imageOverlay(imgPath, imageBounds).addTo(map);
    }
    else {
        imageNew = L.imageOverlay(imgPath, imageBounds).addTo(map);
        console.log('Added imageNew')

    }
    /* Update the image variable to contain the newest simulation on map */
    image = imageNew;
}

/* Functions to update the timeseries data ----------------------------- */
function resetView(){
    myChart.resetZoom();
}



function makeMap2(){
    var crs = new L.Proj.CRS('EPSG:3006','+proj=utm +zone=33 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs',
    {
        resolutions: [
            8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
        ],
        origin: [0,0],
    })

    map = L.map('utbredning', {
        crs: crs
        }
    ).setView([63.834219,20.315930],12)

    L.tileLayer('http://api.geosition.com/tile/osm-bright-3006/{z}/{x}/{y}.png', {
      maxZoom: crs.options.resolutions.length,
      minZoom: 0,
      continuousWorld: true,
      attribution: 'Map data © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>, Imagery © <a href="http://www.kartena.se/">Kartena</a>'
    }).addTo(map);

    /* Loop to add all installed sensors to the current map
    * Code has to be moved to .html so the queryset can be added
    */

    /*
    var x_cord;
    var y_cord;

    {% for dataEntry in sensor_objects %}
    // Get coordinates from the database
    x_cord = dataEntry.x_cord
    y_cord = dataEntry.y_cord

    /* Add markers to the map
    L.marker([x_cord,y_cord]).addTo(mymap);

    {% endfor %}
    */


    /* Manual way to add markers to map
    * Should be depreciated but coordinates are in SWEREF 99
    * in the database so we cannot use the at the moment
    */
    var marker1= L.marker([63.8250972,20.3109672]).addTo(map);
    var marker2= L.marker([63.8263093156, 20.3110416520]).addTo(map);
    var marker3= L.marker([63.8283182582, 20.3143416167]).addTo(map);
    var marker5= L.marker([63.8325499652, 20.3168760740]).addTo(map);
    var marker6= L.marker([63.8360593,20.3163476]).addTo(map);

}




