# Web Directory Scanner with Download Capability

The `web_dir_scanner_with_download.py` script extends the basic functionality of the Web Directory Scanner by not only detecting accessible directories or files on a web server but also downloading content from paths that return a "200 OK" response. It automates the process of checking for the existence of paths listed in a wordlist and downloading the content for further analysis or review.

## Features

- Scans web servers for accessible directories/files using a custom wordlist.
- Downloads content from successful paths.
- Simple command-line interface for easy usage.

## Requirements

- Python 3
- requests library

Before running the script, ensure you have Python 3 installed on your system. You can install the required requests library using pip:


## Usage

To use the script, you need to provide two arguments: the base URL of the web server you wish to scan and the path to your wordlist file.


- `<host>`: The base URL of the web server (e.g., http://example.com).
- `<wordlist_path>`: The path to the wordlist file containing the directories or files to check.

## Preparing Your Wordlist

A wordlist is a simple text file that contains one directory or file path per line. These paths will be appended to the base URL provided to scan the web server. Here’s an example of what the contents of a wordlist file might look like:
Ensure your wordlist is tailored to the specific site or application you're scanning, and it's stored in a location accessible by the script.

## Running the Script

Navigate to the directory containing your script and run it using the following command, replacing `<host>` and `<wordlist_path>` with your values:
The script will iterate through each path in your wordlist, check for a "200 OK" response, and download the content if successful. Downloaded files are saved in a directory named downloads located in the same directory as the script, with filenames derived from their URLs.

## Wordlist Reference

For comprehensive wordlists used for directory and file discovery, consider checking out the following resource:

- [Subdirectories Discover Wordlists on GitHub](https://github.com/aels/subdirectories-discover)

These wordlists can provide a robust starting point for your web directory scanning and content downloading tasks.
