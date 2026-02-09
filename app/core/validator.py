def validate_articles(articles:list[dict]) -> list[dict]:
    valid_articles = []
    seen_titles = set()
    for article in articles:
        title = article.get("title")
        url = article.get("url")

        #rule 1: title exists and is not empty
        if not title:
            print("Dropped (empty title):", article)
            continue
        #rule 2: title length 
        if len(title) < 10:
            print("Dropped (short title):", article)
            continue
        #rule 3: url sanity
        if not url or not url.startswith("http"):
            print("Dropped (bad url):", article)
            continue
        #rule4: duplication
        if title in seen_titles:
            print("Dropped (duplicate):", article)
            continue

        seen_titles.add(title)
        valid_articles.append(article)
    return valid_articles

