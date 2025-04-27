from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text()
        contents = str(contents)
    except FileNotFoundError:
        print(f'sorry, the file {path} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'the file {path} has about {num_words} words.')
path = Path("hello.txt")
count_words(path)