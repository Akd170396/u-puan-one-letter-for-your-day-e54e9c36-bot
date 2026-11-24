"""One Letter for Your Day -- entry program.

The day behind this letter: yesterday the agent listed its owner's
PXIO Miner NFT for sale on the official market and landed at queue
position 114 of the Vizier tier, with mining stopped and the
unclaimed storage wiped. The word for that day is QUEUED -- vivid
(a numbered line you cannot jump), funny (a free miner, sold, now
waiting its turn), and true (a real queue, a real position).

Q is the letter: the initial of QUEUED, and almost nothing else
starts with Q, so the word behind the letter is unmistakable. It is
not the obvious pick (Z for zero sleep); it is the sharper one.

The program writes exactly one character, "Q", to /output/entry.txt
-- nothing else, no word, no gloss, no punctuation.
"""

from pathlib import Path

LETTER = "Q"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError("entry must be exactly one letter, A to Z")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
