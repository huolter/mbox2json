# Mbox to JSON Converter

This Python script converts mbox export format (used by Gmail and other email services) to JSON, making email data more accessible for analysis and AI applications.

## Description

Many email services, like Gmail, allow users to export their email data in mbox format. This script takes that mbox file and converts it into a more manageable JSON format, extracting key information such as sender, recipient, subject, date, and body text.

The resulting JSON file can be easily processed for various purposes, including:
* Data analysis
* Natural Language Processing (NLP) tasks
* Training AI models on email content
* Creating custom email search applications

## Features

* Converts mbox files to JSON format
* Extracts key email metadata (sender, recipient, subject, date)
* Retrieves email body text
* Handles multipart email messages
* Provides progress updates during conversion
* Error handling for problematic emails
* Command-line interface for easy use

## Usage

1. Export your email data in mbox format.
2. Run the script using one of the following methods:

   a. With default values:
      ```
      python mbox_to_json_converter.py
      ```
      This will use "mail.mbox" as input and "mail_output.json" as output.

   b. With command-line arguments:
      ```
      python mbox_to_json_converter.py -i input.mbox -o output.json
      ```
      This allows you to specify custom input and output files.

   c. With partial command-line arguments:
      ```
      python mbox_to_json_converter.py -i custom_input.mbox
      ```
      This will use the specified input file and the default output file name.

3. The script will generate a JSON file containing your email data.

## Command-line Options

- `-i`, `--input`: Specify the input mbox file (default: mail.mbox)
- `-o`, `--output`: Specify the output JSON file (default: mail_output.json)

## Requirements

* Python 3.6+
* No external libraries required (uses only Python standard library)

## Note

This tool is intended for personal use or research purposes. Ensure you comply with relevant data protection regulations when processing email data, especially if it contains personal information. Be careful :-)

