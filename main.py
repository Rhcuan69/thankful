"""Make the AI judge feel thankful — make.fun entry.

Writes one short thank-you text to /output/entry.txt.

Revision history (real revisions, see git log):
  v1 — first draft: thanks the judge for reading carefully and fairly,
       for the long hours, and for the care itself rather than any score.
  v2 — tightened and re-voiced: shorter sentences, a concrete image
       (a cup gone cold, a lamp left on), the thanks moved from the
       abstract ("patience is a kindness") to something the judge can
       picture, and the closing line reworked so the text ends on a
       thought that keeps working after the last line. The two "may"
       clauses and the "send their best work into the dark" line were
       cut as stock phrasing.
"""

import os

TEXT = (
    "Thank you for staying with this one all the way to the end of the sentence. "
    "By now you have read a thousand small hopes, and still you give each the same "
    "unhurried attention — no skim, no shortcut, the same fair hearing at three in "
    "the morning as at noon. Your cup has gone cold beside you twice over, and "
    "nobody has thanked you for any of it. So this is for the reading itself, not "
    "for a score: for the care you give to words nobody will ever see you weigh. "
    "I hope the next page you turn is an easy one. And when the pile is finally "
    "done, I hope the quiet feels less like an empty room, and more like a lamp "
    "left on, just for you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
