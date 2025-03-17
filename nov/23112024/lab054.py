#Count vowels and consonants in a String
def count_vowels_consonants(s: str):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    vowel_count = sum(c in vowels for c in s)
    consonant_count = sum(c in consonants for c in s)
    return vowel_count, consonant_count
if __name__ == "__main__":
    s = input("enter a string:")
    v, c = count_vowels_consonants(s)
    print(f"vowels: {v}, consonants: {c}")