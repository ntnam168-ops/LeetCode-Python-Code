from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

difficulties = ["1_Easy", "2_Medium", "3_Hard"]
stats = {
    d: sum(p.is_file() for p in (ROOT / d).rglob("*"))
    if (ROOT / d).exists() else 0
    for d in difficulties
}

total = sum(stats.values())

table = [
    "| Difficulty | Problems Solved |",
    "|:---:|:---:|",
    f"| 🟢 Easy | {stats['1_Easy']} |",
    f"| 🟡 Medium | {stats['1_Medium']} |",
    f"| 🔴 Hard | {stats['3_Hard']} |",
    f"| **Total** | **{total}** |"
]

content = README.read_text(encoding="utf-8")
start, end = "<!-- STATS:START -->", "<!-- STATS:END -->"

before, remaining = content.split(start, 1)
_, after = remaining.split(end, 1)

README.write_text(
    before + start + "\n\n" + "\n".join(table) + "\n\n" + end + after,
    encoding="utf-8"
)

print(f"Updated statistics: {total} problems")