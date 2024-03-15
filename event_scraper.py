import requests
from bs4 import BeautifulSoup
import sys

MS_LEARN_URL = "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor"
UWS_BASE_URL = "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/"  # Base URL updated

def scrape_event(event_id):
    # Scrape Microsoft Learn content 
    ms_response = requests.get(MS_LEARN_URL)
    ms_soup = BeautifulSoup(ms_response.content, "html.parser")
    table = ms_soup.find('table')  

    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells and cells[0].text.strip() == event_id:  
            legacy_event_id = cells[1].text.strip()
            criticality = cells[2].text.strip()
            summary = cells[3].text.strip()

            output_lines = [
                f"Event ID: {event_id}",
                f"Legacy Event ID: {legacy_event_id}",
                f"Criticality: {criticality}",
                f"Summary: {summary}"
            ]

            # Fetch Ultimate Windows Security page 
            uws_response = requests.get(UWS_BASE_URL, params={'i': 'j', 'EventID': event_id})
            uws_soup = BeautifulSoup(uws_response.content, 'html.parser')

            # Find the link based on the dynamic href attribute
            for link in uws_soup.find_all('a'): 
                if link.get('href') == f"event.aspx?eventid={event_id}":
                    uws_url = UWS_BASE_URL + "event.aspx?eventid=" + event_id 
                    output_lines.append(f"Ultimate Windows Security: {uws_url}")
                    break  
            else:
                output_lines.append("Ultimate Windows Security: Event ID not found")

            print("\n".join(output_lines)) 
            break 
    else:
        print(f"Event ID {event_id} not found on Microsoft Learn.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        event_id = sys.argv[1]  
        scrape_event(event_id)
    else:
        print("Please provide an Event ID as a command-line argument.")
