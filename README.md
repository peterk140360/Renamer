
# Renamer

A Python script to standardize and clean up filenames in a directory. This tool is particularly useful for organizing files with multiple sections separated by " - ", ensuring consistency and clarity in naming conventions.

## URL
https://egiraffe.at

## Features

- **Dynamic Parsing**: Handles filenames with 2, 3, or 4 sections separated by " - ".
- **Flexible Reordering**: Rearranges filename components based on predefined rules.
- **Extension Handling**: Preserves file extensions, even for filenames with multiple dots in their extensions.
- **Compatibility Checks**: Identifies and skips files that don't match the expected naming format.

## Example Transformation

### Input
```
EGIRAFFE Grundlagen der Biomedizinischen Technik VO - user31 - Pruefungsfragenausarbeitung - 2024SS - 59 Seiten
```

### Output
```
EGIRAFFE Grundlagen der Biomedizinischen Technik VO - Pruefungsfragenausarbeitung - 2024SS - user31
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Enter the path to the folder containing the files you want to rename.

### Steps

```bash
# Clone the repository
git clone https://github.com/peterk140360/renamer.git

# Navigate to the directory
cd downloads

# Run the script
python renamer.py
```

4. The script will process the filenames in the specified folder and rename them according to the rules.

## Requirements

- Python 3.x
- `os` module (standard library)

## Notes

- This script assumes filenames follow a structure with " - " as separators.
- Filenames that do not meet the criteria will not be renamed and will produce a log message indicating incompatibility.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by real-world challenges in organizing research and educational documents.

---

Happy organizing! 🎉
