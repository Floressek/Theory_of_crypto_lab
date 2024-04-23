def lz77_encode_corrected_with_user_input():
    # Get user input for dictionary size and buffer size
    dict_size = int(input("Enter the dictionary size: "))
    buf_size = int(input("Enter the buffer size: "))
    text = input("Enter the text to encode: ")

    encoded = []
    index = 0

    while index < len(text):
        # Set the dictionary and buffer boundaries
        dict_start = max(0, index - dict_size)
        buffer_end = index + buf_size
        dictionary = text[dict_start:index]
        buffer = text[index:buffer_end]

        # This will hold the longest match we find during this iteration
        longest_match = {'length': 0, 'offset': 0}

        # Check all possible match positions in the dictionary
        for i in range(len(dictionary)):
            match_length = 0
            while (match_length < len(buffer) and
                   dictionary[i + match_length] == buffer[match_length]):
                match_length += 1
                if i + match_length >= len(dictionary) or index + match_length >= len(text):
                    break

            if match_length > longest_match['length']:
                longest_match = {'length': match_length, 'offset': len(dictionary) - i}

        # Get the next character to output
        next_char_index = index + longest_match['length']
        next_char = text[next_char_index] if next_char_index < len(text) else ''

        # Append the tuple to the encoded list
        encoded.append((longest_match['offset'], longest_match['length'], next_char))

        # Calculate remaining text in a clearer way
        remaining_text = text[buffer_end:] if buffer_end < len(text) else ''

        # Print the current iteration details
        print(
            f'| {dictionary} | {buffer} | {remaining_text} | <{longest_match["offset"]}, {longest_match["length"]}, {next_char}>')

        # Move the index forward in the text
        index += longest_match['length'] + 1 if longest_match['length'] > 0 else 1

    print('Encoded LZ77:', encoded)


# Call the function to get user input and encode text
lz77_encode_corrected_with_user_input()
