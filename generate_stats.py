from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

difficulties = ["Easy", "Medium", "Hard"]
stats = {}

for d in difficulties:
    folder = ROOT / d
    stats[d] = len(list(folder.rglob("*.py"))) if folder.exists() else 0

total = sum(stats.values())

table = [
    "| Difficulty | Problems Solved |",
    "|:---:|:---:|",
    f"| 🟢 Easy | {stats['Easy']} |",
    f"| 🟡 Medium | {stats['Medium']} |",
    f"| 🔴 Hard | {stats['Hard']} |",
    f"| **Total** | **{total}** |"
]

content = README.read_text(encoding="utf-8")

start = "<!-- STATS:START -->"
end = "<!-- STATS:END -->"

before, remaining = content.split(start, 1)
_, after = remaining.split(end, 1)

content = before + start + "\n\n" + "\n".join(table) + "\n\n" + end + after

README.write_text(content, encoding="utf-8")

print(f"Updated statistics: {total} problems")