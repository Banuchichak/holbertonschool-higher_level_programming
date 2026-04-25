import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Invalid input type. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type. Expected list of dictionaries, got {type(attendees).__name__}.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        content = template
        
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            # Replace missing data with N/A
            replacement = str(value) if value is not None else "N/A"
            content = content.replace(f"{{{key}}}", replacement)
        
        output_filename = f"output_{i}.txt"
        
        try:
            with open(output_filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
