def search_by_category(items, category):
    """Return DVDs in the requested category."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Return DVDs whose titles contain keyword."""
    return [dvd for dvd in items if keyword in dvd.title]
