def online_count(word):
    statuses = word
    count = 0
    for name in statuses:
        if statuses[name] == "online":
            count += 1
    return count