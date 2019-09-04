import os
import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))

class NoteBlock(): # TODO: NoteBlock은 init될 때 이미 Note에 속해있어야 한다. 그리고 삭제 시 NoteBlock.instances가 아닌 해당 Note의 instances에서 사라져야 한다. NoteBlock.instances는 복구가능한 휴지통 역할을 할 수 있다. 
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

class Note(): # TODO: 굳이 linked list 형식으로 note 순서를 처리할 필요는 없다. 그냥 리스트에 넣어도 가능하고 훨씬 간편하다. linked 구조는 NoteBlock과 code_line을 연결 할 때는 유용할 것이다. 
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

    def delete_note(self, noteblock): # TODO: Noteblock.instances 와 Note.notes 는 다르다. 구분하여 삭제처리 할 것. (Note는 다양할 수 있음.)
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

note = Note('first note')

note.create_note()
note.create_note()
note.create_note()
note.create_note()

note.notes





