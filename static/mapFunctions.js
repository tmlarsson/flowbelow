/* Functions used for map making --------------------------------------- */

/* Funciton to create base map */
function makeMap(){
    map = L.map("utbredning").setView([63.834219,20.315930], 13);
    makemap(map)
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