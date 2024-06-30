import mailbox
import json
import email
from email.utils import parsedate_to_datetime
import time
from datetime import datetime
from typing import Optional, Dict, List
import argparse

def parse_date(date_string: str) -> Optional[str]:
    """Parse date string to ISO format."""
    try:
        return parsedate_to_datetime(date_string).isoformat()
    except ValueError:
        try:
            return datetime.strptime(date_string, "%d-%b-%Y %H:%M").isoformat()
        except ValueError:
            print(f"Warning: Unable to parse date '{date_string}'. Using None instead.")
            return None

def extract_email_data(message: email.message.Message) -> Dict[str, Optional[str]]:
    """Extract relevant data from an email message."""
    return {
        "from": str(message["from"]),
        "to": str(message["to"]),
        "subject": str(message["subject"]),
        "date": parse_date(str(message["date"])) if message["date"] else None,
        "body": get_email_body(message)
    }

def get_email_body(message: email.message.Message) -> str:
    """Extract the plain text body from an email message."""
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors='replace')
    return message.get_payload(decode=True).decode(errors='replace')

def mbox_to_json(mbox_file: str, json_file: str) -> None:
    """Convert an mbox file to JSON format."""
    print(f"Converting {mbox_file} to JSON...")
    mbox = mailbox.mbox(mbox_file)
    total_emails = len(mbox)
    emails: List[Dict[str, Optional[str]]] = []
    
    start_time = time.time()
    for i, message in enumerate(mbox, 1):
        if i % 100 == 0 or i == total_emails:
            print(f"Processing email {i}/{total_emails} ({i/total_emails*100:.2f}%)")
        try:
            emails.append(extract_email_data(message))
        except Exception as e:
            print(f"Error processing email {i}: {str(e)}")
    
    print(f"Writing {len(emails)} emails to {json_file}...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(emails, f, ensure_ascii=False, indent=2)
    
    end_time = time.time()
    print(f"JSON conversion completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert mbox file to JSON")
    parser.add_argument("-i", "--input", default="mail.mbox", help="Input mbox file (default: mail.mbox)")
    parser.add_argument("-o", "--output", default="mail_output.json", help="Output JSON file (default: mail_output.json)")
    args = parser.parse_args()

    mbox_to_json(args.input, args.output)
