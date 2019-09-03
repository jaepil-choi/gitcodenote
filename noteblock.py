import os
import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))

class NoteBlock():
    def __init__(self, commit_id=None, note_num=None):
        self.note_id = (commit_id, note_num)
        self.created_at = datetime.datetime.now(tz=KST)
        self.note = None
        return 

    def write(self, contents):
        self.note = contents
        return
    
    def read(self):
        return (self.note_id, self.note)

class Note():
    def __init__(self, title):
        self.title = title
        self.notes = []
        return 

    def add_note(self, noteblock):
        self.notes.append(noteblock)
        return

    def read(self):
        print(self.title)
        if self.notes != None:
            for i in self.notes:
                print(i)
        return
        