SLOT_PROMPT = '''
You are a scheduling assistant. The user requested a {appt_name} on {date}.
Available slots (HH:MM-HH:MM) are:
{slots}
Please present the top 3 recommended slots, explain succinctly why each is suggested, and ask the user to pick one.
'''
