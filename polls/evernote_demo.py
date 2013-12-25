"""
Evernote demo.
"""

from django.shortcuts import render_to_response
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter
from evernote.edam.notestore.ttypes import NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder


# Use this in lieu of oauth while testing.
DEV_TOKEN = 'S=s1:U=8d858:E=14a7fe4f6ae:C=1432833cab0:P=1cd:A=en-devtoken:V=2:H=f260c0f5d194f9766854bc6ae53d879d'


def show_evernotes(request):
    # Set up the NoteStore client
    client = EvernoteClient(token=DEV_TOKEN)
    note_store = client.get_note_store()

    note_filter = NoteFilter(order=NoteSortOrder.UPDATED)
    result_spec = NotesMetadataResultSpec(includeTitle=True)

    # Make API calls
    result_list = note_store.findNotesMetadata(
            DEV_TOKEN, note_filter, 0, 100, result_spec)

    data = {
        'notes': result_list.notes
    }
    return render_to_response('polls/show_evernotes.html', data)
