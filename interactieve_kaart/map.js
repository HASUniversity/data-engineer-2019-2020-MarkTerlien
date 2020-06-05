$(document).ready(function() {

	// Define basemaps
	var mapBox = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1,
		accessToken: 'pk.eyJ1IjoibWFya3RlcmxpZW4iLCJhIjoiY2pzMGcwN3liMWU3cTN5bjEyZTljc25jaiJ9.V11hr4mLy77UBhBaM7GeSQ'
	});
	var cartoMap = L.tileLayer('http://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
	});
	
	// Define map overlays
	var wmsLayer = L.tileLayer.wms('http://ows.mundialis.de/services/service?', {
		layers: 'SRTM30-Colored-Hillshade'
	});
	
	// Define overlay with markers
	var HASmarker = L.marker([51.7,5.28]).bindPopup("<h1>Dit is de HAS</h1><a href=\"https://www.has.nl\">Visit our website</a>")
	var markerOverlay = L.layerGroup().addLayer(HASmarker);
	
	// Define map options
	let mapOptions = {
		zoomControl: true,
		center: [52,5],
		zoom: 8,
		layers: [mapBox, markerOverlay]
	}
	
	// Define map global
	var mymap = L.map('kaart', mapOptions);
	
	// Define layer switcher 
	var baseMaps = {
		"MapBox" : mapBox,
		"CartoMap" : cartoMap
	};
	var overlayMaps = {
		"Markers" : markerOverlay,
		"WMS" : wmsLayer
	};
	
	// Ad to map
	L.control.layers(baseMaps,overlayMaps).addTo(mymap);

});

