
console.log('here');

// Stores a list of the markers currently displayed
markers = [];

// Sets the center location of the map
function SetCenter(center) {
  map.setCenter(center);
}

// Removes all existing markers from the map
function ClearMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);  // Remove from map
  }
  markers = [];  // Empty the array
}

// Handler for the "coordinates" form
function CenterOnCoords(e){
  //e.preventDefault();
  ClearMarkers();  // Remove markers if any
  e.preventDefault();
  console.log('Address submitted');
  var lat = $('#lat').val();
  var lon = $('#lon').val();
  if (lat === "" || lon === "") {
    console.log("Not valid");
    window.alert("Need a valid set of coordinates!")
    return false;
  } else {
    // Maps API takes bad parameters and ignores them, so we
    // are good.
    $('#address').val("");
    console.log("Valid Address");
    $.post( "record_request", { type: "coords",
                                lat: lat,
                                lon: lon } );
    SetCenter({lat: parseFloat(lat),
               lng: parseFloat(lon)});
    // We don't want to zoom in too much.
    if (map.getZoom() > 13) {
      map.setZoom(13);
    }
    return true;
  }
}

// When Geocoder is done, it will call this function with the result.
function GeocoderCallback(results, status) {
  if (status === "OK") {
    console.log("We've got " + results.length + " results");
    var bounds = new google.maps.LatLngBounds();
    for(var i = 0; i < results.length; i++) {
      var location = results[i].geometry.location;
      // Create new marker and place it on the map.
      var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: results[i].formatted_address
      });
      // Save marker, we will use it later to remove them.
      markers.push(marker);
      // Increase the area to be visualized if necessary.
      bounds.extend(marker.getPosition());
    }
    map.fitBounds(bounds);
    // We don't want to zoom in too much.
    if (map.getZoom() > 13) {
      map.setZoom(13);
    }
  }
}

// Convert an address into precise locations, one or more, and calls the callback
// function when done.
function GeotagAddress(search_address) {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode(
    {address: search_address}, GeocoderCallback
  );
}

// Handler for the "address" form.
function CenterOnAddress(e){
    ClearMarkers();
    e.preventDefault();
    console.log('Address submitted');
    var address = $('#address').val();
    if (address === "") {
      console.log("Not valid");
      window.alert("Need a valid address!")
      return false;
    } else {
      console.log("Valid Address");
      $('#lat').val("");
      $('#lon').val("");
      $.post( "record_request", { type: "address",
                                  address: address } );
      GeotagAddress(address);
      return true;
    }
}

// Initialization for the Maps APIs
function initialize() {
   var mapOptions = {
     center: { lat: -34.397, lng: 150.644},
     zoom: 8
   };
   map = new google.maps.Map(document.getElementById('map-canvas'),
       mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);

$(document).ready(
  function() {
    $('#coord_form').on('submit', CenterOnCoords);
    $('#address_form').on('submit', CenterOnAddress);
    console.log("done");
  }
);
