def reverse_dna(s):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_s = s[::-1]
    original_chars = [pairs[char] for char in reversed_s]
    return "".join(original_chars)

def main():
    try:
        k = int(input())
        mutated_dna = input()
        if k % 2 == 0:
            print(mutated_dna)
        else:
            original_dna = reverse_dna(mutated_dna)
            print(original_dna)
    except (ValueError, KeyError):
        print("Input tidak valid. Pastikan format input benar dan string hanya berisi A, C, G, T.")

if __name__ == "__main__":
    main()