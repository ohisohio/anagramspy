# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    if(sorted(word1) == sorted(word2)):
        print("The strings are anagrams.")
        return True
    else:
        print("The strings aren't anagrams")
        return False
    



