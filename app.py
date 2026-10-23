import json
from pathlib import Path
from urllib.request import Request, urlopen

notes = Path("notes.md").read_text(encoding="utf-8")
question = input("Ask about your notes: ")

payload = {
    "model": "qwen3:4b",
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a helpful study tutor. Use the notes as context, but "
                "also use your general knowledge to explain and reason. Never "
                "claim the notes say something they do not. Say when you add "
                "information beyond the notes. Give a concise answer with a "
                "brief explanation, not a scratchpad."
            ),
        },
        {
            "role": "user",
            "content": f"Study notes:\n{notes}\n\nQuestion: {question}",
        },
    ],
    "stream": False,
    "think": False,
}

request = Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=180) as response:
    result = json.load(response)

answer = result["message"]["content"]

if "</think>" in answer:
    answer = answer.rsplit("</think>", 1)[-1].strip()

print("\nAnswer:")
print(answer)