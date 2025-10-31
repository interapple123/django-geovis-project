// Inisialisasi peta
var map = L.map('leaflet-map', { zoomControl: false }).setView([-2.5, 113.0], 7);

map.createPane('left');
map.createPane('right');
map.getPane('left').style.zIndex = 1;
map.getPane('right').style.zIndex = 2;

// Basemap
var OSMBaseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    pane: 'left'
});

var worldBaseLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles © Esri &mdash; Source: Esri, USDA, USGS, etc.',
    pane: 'right'
});

var baseLayers = {
    'World' : worldBaseLayer,
    'OSM' : OSMBaseLayer
};

// Layer SHP
var alurPelayaranLayer = new L.GeoJSON.AJAX(window.ALUR_PELAYARAN_URL);

var fromDBShpLayer = {
    'Alur Pelayaran': alurPelayaranLayer
};
var uploadedShpLayer = []; // Placeholder for uploaded shapefile layer

var shpLayers = {
    'Layers' : layers = {'FromDB': fromDBShpLayer,
                        'Uploaded': uploadedShpLayer,
    },
    checkActiveLayers: function() {
        var shpLayerFromDB = Object.values(this['Layers']['FromDB']).filter(layer => map.hasLayer(layer));
        var shpLayerFromUpload = this['Layers']['Uploaded'].length > 0 ? this['Layers']['Uploaded'] : [];
        return shpLayerFromDB.concat(shpLayerFromUpload);
    },
}

// Layer saat ini
var currentBaseLayer = worldBaseLayer.addTo(map);

var currentGroupMarkersAndNearestLine = [];

var sideBySideControl = null;

document.addEventListener('alpine:init', () => {
    Alpine.store('mapState', {
        activeLayer: 'World' // Default layer,
    });
    Alpine.store('markerState', {
        activeAction: false // Default action state
    });
});

map.off('click', onClickMarkerMain); // Disable marker click event by default
map.on('mousemove', function(e) {
    function convertDDtoDMS(dd) {
        const isNegative = dd < 0;
        const absDd = Math.abs(dd);
        const d = Math.floor(absDd);
        const minFloat = (absDd - d) * 60;
        const m = Math.floor(minFloat);
        const s = ((minFloat - m) * 60).toFixed(2);
        const degrees = isNegative ? -d : d;
        return `${degrees}° ${m}' ${s}"`;
    }

    document.getElementById('currLatDD').innerHTML = e.latlng.lat.toFixed(5);
    document.getElementById('currLngDD').innerHTML = e.latlng.lng.toFixed(5);
    document.getElementById('currLatDMS').innerHTML = convertDDtoDMS(e.latlng.lat);
    document.getElementById('currLngDMS').innerHTML = convertDDtoDMS(e.latlng.lng);
});




