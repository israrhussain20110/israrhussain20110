import random
import re
from datetime import datetime

quotes = [
    '"The question of whether a computer can think is no more interesting than the question of whether a submarine can swim." – Edsger Dijkstra',
    '"AI is not just about making machines smarter, it\'s about making people smarter too." – Unknown',
    '"The future is not about man versus machine, but man with machine." – Satya Nadella',
    '"By far, the greatest danger of Artificial Intelligence is that people conclude too early that they understand it." – Eliezer Yudkowsky',
    '"Machine intelligence is the last invention humanity will ever need to make." – Nick Bostrom'
]

new_quote = f"*{random.choice(quotes)}*"

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

updated = re.sub(
    r"<!--START_QUOTE-->.*?<!--END_QUOTE-->",
    f"<!--START_QUOTE-->\n{new_quote}\n<!--END_QUOTE-->",
    readme,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print(f"Updated quote: {new_quote} on {datetime.now()}")
