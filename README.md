# Mbox to JSON Converter

This Python script converts [Gmail's] mbox export format to JSON, making email data more accessible for analysis and AI applications.

## Description

Many email services, like Gmail, allows users to export their email data in mbox format. This script takes that mbox file and converts it into a more manageable JSON format, extracting key information such as sender, recipient, subject, date, and body text.

The resulting JSON file can be easily processed for various purposes, including:
- Data analysis
- Natural Language Processing (NLP) tasks
- Training AI models on email content
- Creating custom email search applications

## Features

- Converts mbox files to JSON format
- Extracts key email metadata (sender, recipient, subject, date)
- Retrieves email body text
- Handles multipart email messages
- Provides progress updates during conversion
- Error handling for problematic emails

## Usage

1. Export your email data in mbox format.
2. Place the mbox file in the same directory as the script.
3. Update the `mbox_file` and `json_file` variables in the script if needed.
4. Run the script: python mbox_to_json_converter.py
5. The script will generate a JSON file containing your email data.

## Requirements

- Python 3.6+
- No external libraries required (uses only Python standard library)

## Note

This tool is intended for personal use or research purposes. Ensure you comply with relevant data protection regulations when processing email data, especially if it contains personal information. Be careful :-)

