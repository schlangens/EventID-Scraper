# Event ID Lookup Tool

This tool scrapes event information from Microsoft Learn and Ultimate Windows Security websites, providing a comprehensive overview of security-related Windows events.

## Dependencies

* Python 3 (https://www.python.org/downloads/)
* requests 
* beautifulsoup4

## Installation

Use `pip` to install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

python event_lookup.py <EventID> 

- Replace <EventID> with the actual Event ID you want to look up.

## Example Output
Event ID: 4625
Legacy Event ID: N/A
Criticality: High
Summary: An account failed to log on.
Ultimate Windows Security: [https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4625](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4625)
