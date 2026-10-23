from pathlib import Path

notes = Path("notes.md").read_text(encoding="utf-8")
search_term = input("Search your notes for: ").strip().lower()

matches = [
    line for line in notes.splitlines()
    if search_term in line.lower()
]

if matches:
    print("\nFound:")
    for line in matches:
        print(line)
else:
    print("\nI couldn't find that in your notes.")