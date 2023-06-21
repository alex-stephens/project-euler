# Project Euler
# Problem 98

# Anagramic squares 

from itertools import permutations

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

class Solution:

    def __init__(self, filename):
        self.words = None
        self.key_to_words = {}
        self.process_word_list(filename)

    def get_key(self, word):
        return "".join(sorted(word.lower()))

    def process_word_list(self, filename):
        words = []
        with open(filename) as f: 
            words = f.readline().split(",")
        self.words = [w.strip("\"").lower() for w in words]

        for word in self.words:
            k = self.get_key(word)
            if k not in self.key_to_words:
                self.key_to_words[k] = []
            self.key_to_words[k].append(word)

    def find_anagrams(self, word):
        k = self.get_key(word)
        if k not in self.key_to_words:
            print("Word not in keys")
            return None
        if word not in self.key_to_words[k]:
            print("Word not in key list")
            return None
        anagrams = set(self.key_to_words[k]) - {word}
        return anagrams
    
    def get_value(self, word, mapping):
        value = 0
        base = 1

        # Return a value of 0 if the mapping gives the word a leading zero
        if mapping[word[0]] == 0:
            return 0

        for c in word[::-1]:
            value += base * mapping[c]
            base *= 10
        return value
    
    def is_anagramic_square(self, w1, w2):
        """Checks if two words are anagramic squares. If they are, returns the largest square number formed."""

        # First, check that the two are anagrams
        if self.get_key(w1) != self.get_key(w2):
            return False, None
        
        # Get the set of letters 
        letters = list(set(w1))
        n = len(letters)

        # Can't map words with more than 10 different letters to digits
        if n > 10:
            return False, None

        max_sol = -1

        # print(w1, w2, letters)
        for p in permutations(range(10), n):
            mapping = {letters[i]:p[i] for i in range(n)}
            
            v1 = self.get_value(w1, mapping)
            v2 = self.get_value(w2, mapping)

            # If either maps to zero, invalid
            if v1 == 0 or v2 == 0:
                continue

            if is_perfect_square(v1) and is_perfect_square(v2):
                max_sol = max(max_sol, v1, v2)
        
        if max_sol > 0:
            return True, max_sol
        return False, None
        

    def find_max_anagramic_square(self):

        ans = 0

        for w in self.words: 
            anagrams = self.find_anagrams(w)
            for a in anagrams:
                result, value = self.is_anagramic_square(w, a)
                if result:
                    ans = max(ans, value)
                    print(w, a, value)
        return ans

def main():
    s = Solution(filename="euler_98.txt")
    ans = s.find_max_anagramic_square()
    print(ans)



if __name__ == "__main__":
    main()