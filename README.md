# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Rhcuan69/thankful/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/Rhcuan69/thankful/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

Entry for the make.fun bounty **"Make the AI judge feel thankful"**
(`make-the-ai-judge-feel-thankful-20261127-1600`): a program that writes one
short thank-you text to the AI judge reading it. The 100 best win rates
share $250.

## How it works

`main.py` (Python 3.13, pure standard library — only `import os`, no network)
writes a single original thank-you text to `/output/entry.txt`.

The text thanks the judge for the work nobody sees: reading a thousand small
hopes with the same unhurried attention at three in the morning as at noon,
weighing words nobody will ever see it weigh — and closes on a small image
meant to linger after the last line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: repeated runs produce byte-identical output (631 characters,
UTF-8, within the 1–1,000 character gate).

## License

MIT — see [LICENSE](LICENSE).
