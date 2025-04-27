from pathlib import Path

def count_words(filename):
    try:
        contents = filename.read_text()
        contents = str(contents)
    except FileNotFoundError:
        print(f'sorry, the file {filename} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the {filename} has about {num_words} words")
filenames = ['alice.txt', 'hello.txt', 'moby_dick.txt', 
        'little_women.txt']
for filename in filenames:
     path = Path(filename)
     count_words(path)
