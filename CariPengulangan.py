def find_longest_repetition(s):
    max_repetition = 0
    current_repetition = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_repetition += 1
        else:
            max_repetition = max(max_repetition, current_repetition)
            current_repetition = 1

    # Handle case where the longest repetition is at the end of the string
    max_repetition = max(max_repetition, current_repetition)

    return max_repetition

# Membaca input dari pengguna
input_string = input().strip()

# Menemukan dan mencetak panjang pengulangan karakter terpanjang
result = find_longest_repetition(input_string)
print(result)
