/**
 * Created by LEE 2 on 6/26/2016.
 */
function initMap()
{
    var map = new google.maps.Map(document.getElementById('map'),
        {
            center: {lat: 43.670218, lng: -79.386782},
            zoom: 3,
            styles: [{
                featureType: 'poi',
                stylers: [{visibility: 'off'}]  // Turn off points of interest.
            }, {
                featureType: 'transit.station',
                stylers: [{visibility: 'off'}]  // Turn off bus stations, train stations, etc.
            }],
            disableDoubleClickZoom: false
        });
    
}
