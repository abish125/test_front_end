"""
Evernote demo.
"""

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter
from evernote.edam.notestore.ttypes import NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


# Use this in lieu of oauth while testing.
DEV_TOKEN = 'S=s1:U=8d858:E=14a7fe4f6ae:C=1432833cab0:P=1cd:A=en-devtoken:V=2:H=f260c0f5d194f9766854bc6ae53d879d'


def show_evernotes(request):
    """Page that shows list of Evernotes.
    """
    result_list = _get_evernote_data()

    data = {
        'notes': result_list.notes
    }
    return render_to_response('polls/show_evernotes.html', data)


def _get_evernote_data():
    """Helper method that gets data.

    Update to give more control to which notes you get.
    """
    # Set up the NoteStore client
    client = EvernoteClient(token=DEV_TOKEN)
    note_store = client.get_note_store()

    note_filter = NoteFilter(order=NoteSortOrder.UPDATED)
    result_spec = NotesMetadataResultSpec(
            includeTitle=True,
            includeCreated=True)

    # Make API call.
    return note_store.findNotesMetadata(
            DEV_TOKEN, note_filter, 0, 100, result_spec)


def evernote_timeline_page(request):
    """Scaffolding for timeline page.

    The rest of the magic happens in JavaScript.
    """
    return render_to_response('polls/evernote_timeline_page.html')


def get_evernote_timeline_data(request):
    """Returns Evernote data in JSON format.

    Meant to be called asynchronously, with result handled in JavaScript.
    """
    # Query Evernote database.
    evernote_result_list = _get_evernote_data()

    # Adapt results to form expected by frontend.
    frontend_note_data = []
    for idx, note in enumerate(evernote_result_list.notes):
        frontend_note_data.append({
            'id': idx,
            'content': note.title,
            'start': note.created,
        })

    # Convert to  JSON.
    json_data = json.dumps(frontend_note_data)

    # Return JSON response.
    return HttpResponse(json_data, mimetype='application/json')
