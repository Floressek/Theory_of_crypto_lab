import math
from collections import Counter

# Wstaw tutaj swój tekst
text = """
Niemiec, Moskal nie osiędzie,
gdy jąwszy pałasza,
hasłem wszystkich zgoda będzie
i ojczyzna nasza.
Marsz, marsz, Dąbrowski
do Polski z ziemi włoski
za Twoim przewodem
złączem się z narodem.
"""

# Zliczanie wystąpień wszystkich znaków w tekście
char_counts = Counter(text)

# Liczba wszystkich znaków w tekście
total_chars = sum(char_counts.values())

# Obliczanie prawdopodobieństw każdego znaku
char_probabilities = {char: count / total_chars for char, count in char_counts.items()}

# Sortowanie słownika prawdopodobieństwa w kolejności malejącej
sorted_probs = sorted(char_probabilities.items(), key=lambda x: x[1], reverse=True)

# Inicjalizacja zmiennych pomocniczych
cum_prob = 0.0  # Zmienna do przechowywania skumulowanego prawdopodobieństwa
table = []  # Lista do przechowywania kroków algorytmu

# Tworzenie kodów dla każdego znaku
for char, prob in sorted_probs:
    code_length = math.ceil(-math.log2(prob))  # Obliczanie długości kodu
    code_binary = format(int(cum_prob * (1 << code_length)), f'0{code_length}b')  # Generowanie kodu binarnego
    log_value = -math.log2(prob)  # Wartość -log(p)

    # Dodawanie kroku do tabeli
    table.append({
        'Znak': repr(char),  # Użycie repr() dla czytelnej reprezentacji znaków, np. spacji
        'Prawdopodobieństwo': f"{prob:.4f}",
        'Stan Kodowy': f"{cum_prob:.4f}",
        '-log(p)': f"{log_value:.2f}",
        'Słowo Kodowe': code_binary
    })

    # Aktualizacja skumulowanego prawdopodobieństwa dla następnego znaku
    cum_prob += prob

# Wydrukowanie wyników
for row in table:
    print(row)


# Przykładowe prawdopodobieństwa i długości słów kodowych dla Shannona i Huffmana
probabilities = {
    ' ': 0.1099, 'z': 0.0942, 'i': 0.0785, 's': 0.0733, 'a': 0.0681, 'e': 0.0576, 'o': 0.0576, '\n': 0.0471,
    'm': 0.0419, 'd': 0.0366, 'w': 0.0314, ',': 0.0262, 'k': 0.0262, 'r': 0.0262, 'c': 0.0209, 'n': 0.0209,
    'y': 0.0209, 'ł': 0.0209, 'ę': 0.0157, 'ą': 0.0157, 'M': 0.0105, 'l': 0.0105, 'g': 0.0105, 'j': 0.0105,
    'p': 0.0105, 'h': 0.0105, 'b': 0.0105, '.': 0.0105, 'N': 0.0052, 't': 0.0052, 'D': 0.0052, 'P': 0.0052, 'T': 0.0052
}

# Przykładowe długości kodów dla Shannona (zebrane z poprzednich odpowiedzi)
shannon_lengths = {
    ' ': 4, 'z': 4, 'i': 4, 's': 4, 'a': 4, 'e': 5, 'o': 5, '\n': 5,
    'm': 5, 'd': 5, 'w': 5, ',': 6, 'k': 6, 'r': 6, 'c': 6, 'n': 6,
    'y': 6, 'ł': 6, 'ę': 6, 'ą': 6, 'M': 7, 'l': 7, 'g': 7, 'j': 7,
    'p': 7, 'h': 7, 'b': 7, '.': 7, 'N': 8, 't': 8, 'D': 8, 'P': 8, 'T': 8
}

# Przykładowe długości kodów dla Huffmana (przygotowane według Twojego opisu)
huffman_lengths = {
    'z': 3, 'o': 4, ' ': 3, 'e': 4, 'w': 5, 'a': 4, 's': 4, 'i': 4,
    'd': 5, 'n': 6, 'c': 6, 'ł': 6, 'm': 5, 'y': 6, 'l': 7, 'p': 7,
    ',': 5, 'r': 5, 'k': 5, 'ą': 6, 'ę': 6, 'N': 7, 't': 7, 'T': 7,
    'b': 7, 'M': 7, 'g': 7, 'h': 7, 'j': 7, '.': 7, 'D': 8, 'P': 8, '\n': 4
}

# Obliczenie średniej długości dla Shannona
shannon_average = sum(probabilities[char] * shannon_lengths[char] for char in probabilities)

# Obliczenie średniej długości dla Huffmana
huffman_average = sum(probabilities[char] * huffman_lengths[char] for char in probabilities)

print(shannon_average, huffman_average)