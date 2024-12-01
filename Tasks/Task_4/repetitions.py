def get_frequency(words):
    counts = {}  
    for word in words:  
        counts[word] = counts.get(word, 0) + 1  
    return counts  

if __name__ == '__main__':
    words = ["Welcome", "awdy", "Hi", "awdy", "No", "Hi", "No", "awdy", "No", "awdy"]
    print(get_frequency(words))  
