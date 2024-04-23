
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
Enter the dictionary size: 6
Enter the buffer size: 4
Enter the text to encode: abracadabra
```

Output:
```
|  | abra | bracadabra | <0, 0, a>
| a | brac | racadabra | <0, 0, b>
...
Encoded LZ77: [(0, 0, 'a'), (0, 0, 'b'), ...]
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `https://your-repository-url` and `your-repository-directory` with your actual repository URL and directory name. This `README.md` provides a comprehensive guide for users to understand what the project does, how to set it up, and how to use it. Adjust the text as needed to better fit your project specifics or additional features.
