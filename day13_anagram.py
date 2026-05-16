def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    hashmap = {}

    for ch in s1:
        hashmap[ch] = hashmap.get(ch, 0) + 1

    for ch in s2:

        if ch not in hashmap:
            return False

        hashmap[ch] -= 1

        if hashmap[ch] == 0:
            del hashmap[ch]

    return len(hashmap) == 0


print(is_anagram("listen", "silent"))