import os
import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))

class NoteBlock(): # TODO: NoteBlock은 init될 때 이미 Note에 속해있어야 한다. 그리고 삭제 시 NoteBlock.instances가 아닌 해당 Note의 instances에서 사라져야 한다. NoteBlock.instances는 복구가능한 휴지통 역할을 할 수 있다. 
    instances = []

    def __init__(self, commit_id=None, file_name=None, note_num=None):
        self.note_id = (commit_id, file_name, note_num)
        self.created_at = datetime.datetime.now(tz=KST)
        self.note = None
        
        self.previous = NoteBlock.instances[-1] if NoteBlock.instances != [] else None
        NoteBlock.instances.append(self)
        
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

    def delete_note(self, noteblock): # TODO: Noteblock.instances 와 Note.notes 는 다르다. 구분하여 삭제처리 할 것. (Note는 다양할 수 있음.)
        if NoteBlock.instances == []:
            print('NoteBlock instances is empty.')
            return 

        index = NoteBlock.instances.index(noteblock)
        if index != (len(NoteBlock.instances) - 1):
            NoteBlock.instances[index+1].previous = noteblock.previous
            NoteBlock.instances.remove(noteblock)
            self.notes.remove(noteblock)
        else:
            NoteBlock.instances.remove(noteblock)
            self.notes.remove(noteblock)
        return

    def read(self):
        print(self.title)
        if self.notes != None:
            for i in self.notes:
                print(i)
        return

# note = Note('first note')
# spam = NoteBlock()
# ham = NoteBlock()
# egg = NoteBlock()
# foo = NoteBlock()
# bar = NoteBlock()

# note.add_note(spam)
# note.add_note(ham)
# note.add_note(egg)
# note.add_note(foo)
# note.add_note(bar)

# note.read()
# note.delete_note(spam)
# note.read()
# note.delete_note(egg)
# note.read()
# note.delete_note(bar)
# note.read()