def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    hashset = {}
    result = 0

    for character in text:
        if character in hashset:
            hashset[character] += 1
        else:
            hashset[character] = 1

    for i in hashset.values():
        if i != 1:
            result += 1

    return result

print(duplicate_count('abcdeaB'))
