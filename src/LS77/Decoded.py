def lz77_decode(encoded):
    decoded = ''
    for offset, length, next_char in encoded:
        # Find the start of the matched string in the already decoded text
        start = len(decoded) - offset
        # Append the matched string to the decoded text
        if length > 0:
            matched_string = decoded[start:start + length]
            decoded += matched_string
        # Append the next character if it's not None
        if next_char:
            decoded += next_char

        # For debugging, print the step by step decoding
        print(f"Decoded so far: '{decoded}'")

    return decoded


# Decoding the example encoded text from LZ77
encoded_example = [(0, 0, 'a'), (0, 0, 's'), (0, 0, 'd'), (3, 3, 'a'), (3, 3, 's'), (3, 3, 'd'), (3, 3, '')]
original_text = lz77_decode(encoded_example)
print('Decoded text:', original_text)
