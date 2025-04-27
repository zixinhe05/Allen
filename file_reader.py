from pathlib import Path
path = Path('text_files/pi_digits.txt')
contents = path.read_text()
contents1 = contents.replace("good","better")
print(contents1)