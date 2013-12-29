/**
 * Basic demo of dynamically-updating timeline view using Evernote data.
 */

// Create the sd "smarter doctor" namespace if not yet available.
var sd = sd || {};


/** Backbone view object to wrap the timeline. */
sd.EvernoteTimelineView = Backbone.View.extend({

    initialize: function() {

        // Element to which we attach the timeline.
        this.timelineHookEl = $('#timeline-hook')[0];

        // Options to timeline widget.
        this.options = {};

        // Timeline object attached to this.
        this.timeline = null;

        // Load the initial data.
        this.updateTimelineData();
    },

    /**
     * Update the timeline with new data.
     *
     * For now, this just empties the div and gets new data from the server.
     * Eventually we'll want to do per day requests or something like that.
     */
    updateTimelineData: function() {
         // Remove the previous timeline object.
        $('#timeline-hook').empty();

        // Make a request for data from the server and redraw the timeline
        // once received.
        $.get('/polls/_/get_evernote_timeline_data/', _.bind(function(data) {
            // Convert the data into an object.
            var parsedData = JSON.parse(data);

            // Create and render a new timeline object.
            this.timeline = new vis.Timeline(this.timelineHookEl, parsedData,
                    this.options);

        }, this));
    },
});


// JavaScript starts running here on page load complete.
$(document).ready(function() {
    var view = new sd.EvernoteTimelineView();
});
