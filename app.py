import re
from pathlib import Path

notes = Path("notes.md").read_text(encoding="utf-8")
question = input("Ask about your notes: ").lower()

stop_words = {"what", "is", "a", "an", "the", "of", "to", "in", "my", "explain"}
question_words = {
    word for word in re.findall(r"[a-z0-9]+", question)
    if word not in stop_words
}

results = []

for line in notes.splitlines():
    line_words = set(re.findall(r"[a-z0-9]+", line.lower()))
    score = len(question_words & line_words)

    if score > 0:
        results.append((score, line))

results.sort(key=lambda result: result[0], reverse=True)

if results:
    print("\nMost relevant notes:")
    for score, line in results[:3]:
        print(f"- {line}")
else:
    print("\nI couldn't find anything relevant in your notes.")