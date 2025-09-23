import hashlib

WORDLIST = "test.txt"
HASHLIST = "hashes.txt"
HASHES = []

def hashing(text):
    return hashlib.new("sha256", text.encode("utf-8")).hexdigest()

def open_wordlist(file):
    with open(file, "r") as file:
        for hash in file:
            hash = hashing(hash.strip())
            HASHES.append(hash)

def write_hashes(file):
    with open(file, "w") as file:
        for hash in HASHES:
            file.write((hash + "\n"))

if __name__ == "__main__":
    open_wordlist(WORDLIST)
    write_hashes(HASHLIST)
    print(f"Hashes written from {WORDLIST} to {HASHLIST}")