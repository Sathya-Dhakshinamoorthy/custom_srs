import frappe

def validate(doc,event):
    validate_replied(doc)

def validate_replied(doc):

    if doc.status in ["Open", "Replied", 'Do Not Disturb']:
        
        if doc.custom_view_follow_up_details_copy:
            doc.status = 'Replied'

            if doc.custom_view_follow_up_details_copy[-1].__dict__["status"] == "Do Not Disturb":
                doc.status = 'Do Not Disturb'
        
        else:
            doc.status = 'Open'