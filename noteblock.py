import os
import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))

class NoteBlock(): 
    def __init__(self, belongs_to, commit_id=None, file_name=None, note_num=None):
        self.note_id = (commit_id, file_name, note_num)
        self.created_at = datetime.datetime.now(tz=KST)
        self.note = None
        self.belongs_to = belongs_to
        belongs_to.notes.append(self)
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

    def create_note(self):
        noteblock = NoteBlock(self)
        self.notes.append(noteblock)
        return

    def add_note(self, noteblock):
        self.notes.append(noteblock)
        return

    def delete_note(self, noteblock): 
        if self.notes == []:
            print('The note is empty.')
            return
        elif noteblock not in self.notes:
            print("ERROR: The noteblock doesn't belong to this note.")
            return
        self.notes.remove(noteblock)
        print('The noteblock has been deleted.')
        return

    def read(self):
        print(self.title)
        if self.notes != None:
            for i in self.notes:
                print(i)
        return






