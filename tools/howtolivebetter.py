"""Extract short entry titles from a local clone of eternity4719/HowToLiveBetter (CC BY 4.0).

The Chinese page shows one at random under the date. The line sits in a casual greeting, so titles
longer than MAX_LEN characters and titles on serious topics (SERIOUS: suicide, depression and other
mental health crises, crime, violence, gambling, fraud, ...) are left out. Other health advice
(screening, sexual health, first aid, disability care) and the sections on bereavement and setbacks stay.

    git clone --depth 1 https://github.com/eternity4719/HowToLiveBetter /tmp/hlb
    python3 tools/howtolivebetter.py /tmp/hlb
"""

import json
import re
import subprocess
import sys
from pathlib import Path

MAX_LEN = 40
SERIOUS = re.compile(
    r"代价|自杀|拿死|抑郁|精神|心理科|心理门诊|心理测评|12356|12355|嫖娼|家暴|"
    r"赌|诈骗|电诈|传销|羁押|无罪|判刑|拘留|刑事|行贿|农药")
OUT = Path(__file__).resolve().parent.parent / "zh" / "howtolivebetter.json"


def main(repo: str) -> None:
    root = Path(repo)
    items = []
    for path in sorted((root / "book").glob("[0-9][0-9]-*.md")):
        section = int(path.name[:2])
        for number, title in re.findall(r"^### (\d+)\. (.+)$", path.read_text(encoding="utf-8"), re.M):
            title = title.strip()
            if len(title) <= MAX_LEN and not SERIOUS.search(title):
                items.append([section, int(number), title])
    commit = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%h %cs"],
                            capture_output=True, text=True, check=True).stdout.split()
    data = {"source": "https://github.com/eternity4719/HowToLiveBetter", "license": "CC BY 4.0",
            "commit": commit[0], "date": commit[1], "items": items}
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}: {len(items)} entries from {commit[0]} ({commit[1]})")


if __name__ == "__main__":
    main(sys.argv[1])
