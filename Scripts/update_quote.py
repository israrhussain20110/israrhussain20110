import random
import re
from datetime import datetime
from pathlib import Path
import sys

quotes = [
    '"The question of whether a computer can think is no more interesting than the question of whether a submarine can swim." – Edsger Dijkstra',
    '"AI is not just about making machines smarter, it\'s about making people smarter too." – Unknown',
    '"The future is not about man versus machine, but man with machine." – Satya Nadella',
    '"By far, the greatest danger of Artificial Intelligence is that people conclude too early that they understand it." – Eliezer Yudkowsky',
    '"Machine intelligence is the last invention humanity will ever need to make." – Nick Bostrom'
]

def main():
    new_quote = f"*{random.choice(quotes)}*"
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("ERROR: README.md not found in the current working directory.", file=sys.stderr)
        sys.exit(2)

    readme = readme_path.read_text(encoding="utf-8")

    updated = re.sub(
        r"<!--START_QUOTE-->.*?<!--END_QUOTE-->",
        f"<!--START_QUOTE-->\n{new_quote}\n<!--END_QUOTE-->",
        readme,
        flags=re.DOTALL
    )

    if updated == readme:
        print("No changes made to README.md (quote block not found or no change).")
        return

    readme_path.write_text(updated, encoding="utf-8")
    print(f"Updated quote: {new_quote} on {datetime.utcnow().isoformat()}")

if __name__ == "__main__":
    main()
