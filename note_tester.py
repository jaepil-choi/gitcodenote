from git_importer import get_files, get_note_nums
from noteblock import NoteBlock, Note

note0 = "Hello World"
note1 = "Goodbye World"

sha = "55c5b4976d423677345f053e1b20274130a95cb4"

notebook = Note("My first code note")
notebook.create_note(sha, "samplecode.py", 1)
notebook.create_note(sha, "samplecode.py", 2)
notebook.notes[0].write(note0)
notebook.notes[1].write(note1)
notebook.read()

notebook.notes