from __future__ import annotations

import re

_WORD_RE = re.compile(r"[A-Za-z0-9']+")

def top_k_words(text: str, stopwords: set[str], k: int = 3) -> list[tuple[str, int]]:
    """Return the k most frequent normalized words, excluding stopwords.

    Rules:
      - case-insensitive
      - ignore punctuation (words matched by _WORD_RE)
      - exclude stopwords
      - sort by count desc, then word asc

    Returns:
      List of (word, count)
    """
    # TODO: implement
    raise NotImplementedError
