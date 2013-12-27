/**
 * Basic demo of dynamically-updating timeline view using Evernote data.
 */

// Create the sd "smarter doctor" namespace if not yet available.
var sd = sd || {};


/**
 * Update the timeline with new data.
 *
 * For now, this just empties the div and gets new data from the server.
 * Eventually we'll want to do per day requests or something like that.
 */
sd.updateTimelineData = function() {
     // Remove the previous timeline object.
    $('#timeline-hook').empty();

    // Make a request for data from the server and redraw the timeline
    // once received.
    $.get('/polls/_/get_evernote_timeline_data/', function(data) {
        // Convert the data into an object.
        // JSON should be available on most modern browsers (at least Chrome).
        var parsedData = JSON.parse(data);

        // Create and render a new timeline object.
        sd.timeline = new vis.Timeline(sd.containerEl, parsedData, sd.options);

    });
};


// JavaScript starts running here on page load complete.
$(document).ready(function() {
    // Put all the objects under the sd namespace.
    // TODO: Use proper object patterns.
    sd.containerEl = $('#timeline-hook')[0];
    sd.options = {};

    // Perform initial update.
    sd.updateTimelineData();
});
