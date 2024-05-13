
# LZ77 Compression and Shannon Entropy Calculator

This repository contains Python implementations of the LZ77 compression algorithm and a Shannon entropy calculator. These tools are designed to help understand and analyze the efficiency of text compression and the inherent information content in data.

## Features

- **LZ77 Compression**: Encode text using the LZ77 algorithm, which is useful for understanding basic concepts in data compression techniques.
- **Shannon Entropy Calculator**: Compute the Shannon entropy for a given text to understand the theoretical limits of lossless compression for that text.

## Getting Started

To use these scripts, you will need Python installed on your computer. These scripts are tested with Python 3.8 but should be compatible with other Python 3.x versions.

### Prerequisites

Ensure you have Python installed. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

Clone this repository to your local machine using:

```bash
gh repo clone Floressek/Theory_of_crypto_lab
cd your-repository-directory
```

### Usage

#### LZ77 Compression

To encode text using the LZ77 algorithm, run the `Encoded.py` script. You will be prompted to enter the dictionary size, buffer size, and the text you want to compress.

```bash
python Encoded.py
```

Follow the prompts to input your parameters and text.

#### Shannon Entropy Calculator

To calculate the Shannon entropy of a given text, run the `Shannon_result_table.py` script. You will need to input the text for which you want the entropy calculated.

```bash
python Shannon_result_table.py
```

### Examples

Here's how you can use the LZ77 encoding script:

```bash
Enter the dictionary size: 15
Enter the buffer size: 5
Enter the text to encode: BAADAADDDBEEDAAEAADAABDDA
```

Output:
```
Dictionary           | Buffer               | Remaining            | Match               
------------------------------------------------------------------------------------
                     | BAADA                | ADDDBEEDAAEAADAABDDA | <0, 0, B>
B                    | AADAA                | DDDBEEDAAEAADAABDDA  | <0, 0, A>
BA                   | ADAAD                | DDBEEDAAEAADAABDDA   | <1, 1, D>
BAAD                 | AADDD                | BEEDAAEAADAABDDA     | <3, 3, D>
BAADAADD             | DBEED                | AAEAADAABDDA         | <5, 1, B>
BAADAADDDB           | EEDAA                | EAADAABDDA           | <0, 0, E>
BAADAADDDBE          | EDAAE                | AADAABDDA            | <1, 1, D>
BAADAADDDBEED        | AAEAA                | DAABDDA              | <12, 2, E>
AADAADDDBEEDAAE      | AADAA                | BDDA                 | <15, 5, B>
DDBEEDAAEAADAAB      | DDA                  |                      | <15, 2, A>
Encoded LZ77: [(0, 0, 'B'), (0, 0, 'A'), (1, 1, 'D'), (3, 3, 'D'), (5, 1, 'B'), (0, 0, 'E'), (1, 1, 'D'), (12, 2, 'E'), (15, 5, 'B'), (15, 2, 'A')]
Amount of encoded words: 10

```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
