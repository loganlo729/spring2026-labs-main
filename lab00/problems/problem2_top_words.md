## Problem 2: Top Words (Normalized)

Write:
```python
def top_k_words(text: str, stopwords: set[str], k: int = 3) -> list[tuple[str, int]]:
    ...
```

Rules:
- case-insensitive
- ignore punctuation
- exclude stopwords
- return (word, count) sorted by count desc, then word asc
