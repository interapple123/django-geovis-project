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

function drawMarker(lat, lng){
    var newMarker = L.marker([lat, lng]).on('click', e => isMarkerActive() ? e.target.remove() : null).addTo(map);
    currentMarkers.push(newMarker);
}