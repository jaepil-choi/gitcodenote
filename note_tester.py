from git_importer import get_files, get_note_nums
from noteblock import NoteBlock, Note

files_list = get_files(0) 
print(files_list)

note_nums_list = get_note_nums(files_list[0])
print(note_nums_list)

files_list[0].sha, files_list[0].filename


note0 = input("Write content for the first code line")
note1 = input("Write content for the second code line")

notebook = Note("My first code note") # TODO: Bug in linking note to noteblock.
notebook.create_note(files_list[0].sha, files_list[0].filename, 0)
notebook.create_note(files_list[0].sha, files_list[0].filename, 1)
notebook.notes[0].write(note0)
notebook.notes[1].write(note1)
notebook.read()