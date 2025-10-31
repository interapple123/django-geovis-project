function mapZoomIn() {
    map.zoomIn();
}

function mapZoomOut() {
    map.zoomOut();
}

function changeLayerHandler(choice) {
    if (map.hasLayer(currentBaseLayer)) { // assuming 'currentBaseLayer' holds the active base layer object
        map.removeLayer(currentBaseLayer);
    }

    var newBaseLayer = baseLayers[choice].addTo(map);
    currentBaseLayer = newBaseLayer;

    Alpine.store('mapState').activeLayer = choice;
}
// function map

function markerToggle() {
    Alpine.store('markerState').activeAction = !isMarkerActive();
    if (!isMarkerActive()) {
        map.off('click', onClickMarkerMain);
    } else {
        map.on('click', onClickMarkerMain);
    }
}

function onClickMarkerMain(e) {
    if (isShiftKeyPressed(e)) {
        currentGroupMarkersAndNearestLine.forEach(function(MarkerAndNearestLine) {
            map.removeLayer(MarkerAndNearestLine);
        });
        currentGroupMarkersAndNearestLine = [];
    } else {
        drawMarkerOrNearestLine(e.latlng.lat, e.latlng.lng);
    }
}

function shpLayerHandler(layerName) {
    if (map.hasLayer(shpLayers['Layers']['FromDB'][layerName])) {
        map.removeLayer(shpLayers['Layers']['FromDB'][layerName]);
    }
    else {
        shpLayers['Layers']['FromDB'][layerName].addTo(map);
    }
}

async function updateUploadedShpLayer() {
    try {
        var uploadedShpLayer = new L.GeoJSON.AJAX('statics/api/upload/geojson/').addTo(map);
        shpLayers['Layers']['Uploaded'].push(uploadedShpLayer);
    } catch (error) {
        console.error('Error fetching uploaded shapefile:', error);
    }
}

function placeMarker() {
    try {
        fetch('statics/api/input/markercoords/')
        .then(response => response.json())
        .then(data => {
            var lat = parseFloat(data.latitude);
            var lng = parseFloat(data.longitude);
            if (!isNaN(lat) && !isNaN(lng)) {
                drawMarkerOrNearestLine(lat, lng);
            } else {
                console.error('Invalid coordinates received:', data);
            }
        })
        .catch(error => {
            console.error('Error fetching marker coordinates:', error);
        });
    } catch (error) {
        console.error('Error placing marker from input coordinates:', error);
    }
}

function sideBySideToggle() {
    if (sideBySideControl) {
        map.removeControl(sideBySideControl);
        sideBySideControl = null;
    } else {
        sideBySideControl = L.control.sideBySide(baseLayers['World'].addTo(map), baseLayers['OSM'].addTo(map)).addTo(map);
    }
}