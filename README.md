# BW Thumbnail Extractor

A python program to extract thumbnail images of BW files (files having the extension .bw).

## Getting Started

### Requirements

- [Python 3](https://www.python.org/downloads/)

### Dependencies

- (No dependencies)

### Configuration

The configuration file `config.ini` should be placed in the folder of the executable.
There are 2 sessions, `USER` and `DEFAULT`.

1. `USER`

- `path`: path of the files to be loaded.

2. `DEFAULT` (no need to change the content)
   - `db_extension`: format of the files to be loaded.
   - `image_extension`: format of the thumbnail files to be generated.

### Executing program

1. Run the Python code directly:

```bash
python main.py
```

or

```bash
python3 main.py
```

2. Run the executable (built separately).

### Expected behavior

1. Locate all the files of the extension `db_extension` under the folder `path` (including all subfolders).
2. For each file located, check if the file of the same name with the extension `image_extension` is already found. If not, try extracting a thumbnail file with the file name aforementioned.
   - If the file is stored in a cloud storage and is not available locally, it will be downloaded first before extracting a thumbnail from it.
   - Skip to the next file if the extraction fails.

### Log files

A log file will be generated under the folder where this program is executed.
`BwExtract_va.b_yyyymmddhhmmss.log`

- `a.b` is the version number of this program.
- `yyyymmddhhmmss` is the local time when this program is started.

## Author

Issac Tai (issactai0124@gmail.com)

## Version History

- 1.0
  - Release
  - Fix logging content and format
  - Added more error checks
- 0.21
  - Fix logging content
  - Fix path of config
- 0.20
  - Prototype
- 0.10
  - Initial release of demo
