function isMarkerActive() {
    return Alpine.store('markerState').activeAction
}

function isShiftKeyPressed(e) {
    if (e.originalEvent.shiftKey) {
        return true;
    } else {
        return false;
    }
}

function drawMarkerOrNearestLine(lat, lng){
    activeShpLayers = shpLayers.checkActiveLayers();
    var newMarker = L.marker([lat, lng]).on('click', e => isMarkerActive() ? e.target.remove() : null);

    if (activeShpLayers.length === 0) {
        currentGroupMarkersAndNearestLine.push(newMarker.addTo(map));
    } else {
        var closestShpLayers, closestShpLayer, closestShpLayerPoint, closestShpLayerDistance, polylinePoints;
        closestShpLayers = L.GeometryUtil.nClosestLayers(map, activeShpLayers, L.latLng(lat, lng), 1)[0];
        closestShpLayer = closestShpLayers.layer
        closestShpLayerPoint = closestShpLayers.latlng
        closestShpLayerDistance = closestShpLayers.distance

        polylinePoints = [closestShpLayerPoint, L.latLng(lat, lng)]

        var newPolyline = L.polyline(polylinePoints, {color: 'red'});
        var newMarkerAndNearestLine = L.featureGroup([newMarker, newPolyline]).on('click', e => isMarkerActive() ? e.target.remove() : null).addTo(map);

        currentGroupMarkersAndNearestLine.push(newMarkerAndNearestLine);
    }
}