# BW Thumbnail Extractor

A python script to extract thumbnail images of BW files (files having the extension as .bw).

Currently this repo contains only a script showing how a thumbnail can be extracted from a BW file.

## Getting Started

### Requirements

- [Python 3](https://www.python.org/downloads/)

### Dependencies

- (No dependencies)

### Executing program

- Change line 4 of main.py: replace the path of BW file
  - change only [path of bw file] in [r"path of bw file"], for example

```bash
path = r"C:\Users\Test User\Designer files\test.bw" ### change this
```

- run the Python script

```bash
python main.py
```

## Motivation

In the fashion industry, one popular file format for desigmers to work is the Browzwear garment file format (BW).

For a machine with a suitable software installed (e.g. [VStitcher](https://browzwear.com/products/v-stitcher)), a thumbnail is displayed when a BW file locally available is selected in a file browser.

Companies may rely on cloud storages (e.g. [Microsoft OneDrive](https://www.microsoft.com/en/microsoft-365/onedrive/online-cloud-storage/)) so BW files can be accessed easily among staffs.

However most cloud storages do not support BW files, and thumnbail previews will not be displayed until the files are downloaded.

This application aims to extract thumbnails as store as image files of the same name so that previews are available on cloud storages.

## Author

Issac Tai [E-mail](issactai0124@gmail.com)

## Version History

- 0.1
  - Initial release of demo
