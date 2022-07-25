"""
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters.
    No two characters may map to the same character, but a character may map to itself.
"""
MAX_CHARS = 256


class IsomorphicStringsClass:
    def __init__(self):
        pass

    def isIsomorphic(self, s, t):
        marked = [False] * MAX_CHARS
        mapy = [-1] * MAX_CHARS
        for i in range(len(t)):
            if mapy[ord(s[i])] == -1:
                if marked[ord(t[i])]:
                    return False
                marked[ord(t[i])] = True
                mapy[ord(s[i])] = t[i]
            elif mapy[ord(s[i])] != t[i]:
                return False
        return True
