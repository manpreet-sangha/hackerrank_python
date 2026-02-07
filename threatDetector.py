import math
import os
import random
import re
import sys

#
# Complete the 'threatDetector' function below.
#
# The function accepts STRING_ARRAY textMessages as parameter.
#

def threatDetector(textMessages):
    # Write your code here
    
    def find_palindromes(text):
        """Find all palindromes with 3 or more characters in the text."""
        palindromes = []
        n = len(text)
        
        # Check all substrings of length 3 or more
        for i in range(n):
            for j in range(i + 3, n + 1):
                substring = text[i:j]
                if substring == substring[::-1]:
                    palindromes.append(substring)
        
        return palindromes
    
    def get_label(score):
        """Assign label based on score."""
        if score == 0:
            return "Ignore"
        elif 1 <= score <= 10:
            return "Possible"
        elif 11 <= score <= 40:
            return "Probable"
        elif 41 <= score <= 150:
            return "Escalate"
        else:
            return "Ignore"
    
    for message in textMessages:
        # last 3 characters are the symbol
        symbol = message[-3:]
        # exclude the symbol from the text content
        text_content = message[:-3]
        
        # detect palindromes in the text content
        palindromes = find_palindromes(text_content.lower())
        
        # Check if there's a threat (2 or more palindromes)
        if len(palindromes) >= 2:
            # Calculate cardinality score (sum of lengths)
            score = sum(len(p) for p in palindromes)
            label = get_label(score)
        else:
            label = "Ignore"
        
        print(f"{symbol} {label}")

if __name__ == '__main__':
    textMessages_count = int(input().strip())

    textMessages = []

    for _ in range(textMessages_count):
        textMessages_item = input()
        textMessages.append(textMessages_item)

    threatDetector(textMessages)