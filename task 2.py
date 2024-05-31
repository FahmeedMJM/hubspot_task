import requests
import json


headers = {
    'Authorization': 'Bearer pat-na1-0ce3692a-9717-4fa6-9447-6ef77c94fe82',
    'Content-Type': 'application/json'
}

def fetch_tickets(headers):
    url = 'https://api.hubapi.com/crm/v3/objects/tickets?associations=emails'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text  # Return the parsed JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Output any HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Output any other errors

def fetch_email(headers):
    url = 'https://api.hubapi.com/crm/v3/objects/email'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text  # Return the parsed JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Output any HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Output any other errors


def parse_and_display_tickets(tickets_json):
    # Parse the JSON string into a dictionary
    tickets = json.loads(tickets_json)
    
    # Check if the 'results' key is in the tickets dictionary
    if 'results' in tickets:
        for ticket in tickets['results']:
            # Extract ticket properties
            ticket_id = ticket.get('id', 'No ID')
            properties = ticket.get('properties', {})
            subject = properties.get('subject', 'No Subject')
            status = properties.get('hs_pipeline_stage', 'No Status')
            created_at = properties.get('createdAt', 'No Creation Date')
            
            # Display the ticket information
            print(f"Ticket ID: {ticket_id}")
            print(f"Subject: {subject}")
            print(f"Status: {status}")
            print(f"Created At: {created_at}")
            print("-" * 40)
    else:
        print("No tickets found.")

def parse_and_display_emails(email_json):
    # Parse the JSON string into a dictionary
    emails = json.loads(email_json)
    
    # Check if the 'results' key is in the tickets dictionary
    if 'results' in emails:
        for email in emails['results']:
            # Extract email properties
            email_id = email.get('id', 'No ID')
            properties = email.get('properties', {})
            subject = properties.get('subject', 'No Subject')
            status = properties.get('hs_pipeline_stage', 'No Status')
            created_at = email.get('createdAt', 'No Creation Date')
            
            # Display the email information
            print(f"Email ID: {email_id}")
            print(f"Subject: {subject}")
            print(f"Created At: {created_at}")
            print("-" * 40)
    else:
        print("No email found.")


# Fetch and print tickets
tickets = fetch_tickets(headers)
if tickets:
    print(tickets)
    print(parse_and_display_tickets(tickets))
else:
    print("Failed to fetch tickets.")

emails = fetch_email(headers)
if emails:
    print(emails)
    print(parse_and_display_emails(emails))

else:
    print("Failed to fetch emails.")
