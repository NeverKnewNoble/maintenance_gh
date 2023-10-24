# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class MaintenanceScheduling(Document):
#     pass

#ORIGINAL ON SUBMIT FOR TRACKER WHICH IS PATRICK"S CODE >>>>>>>>>>>>>>>>>>>>>

# @frappe.whitelist()
# def create_scheduling_tracker_documents(doc):
#     # Deserialize the JSON string into a Python dictionary
#     doc = frappe.parse_json(doc)
#     if doc.get("appointment"):
#         for row in doc.get("appointment"):
#             scheduling_tracker_doc = frappe.new_doc("Schedule Tracker")
#             scheduling_tracker_doc.sector_name = row.get("sector_name")
#             scheduling_tracker_doc.description_scheduling = row.get("description_scheduling")
#             scheduling_tracker_doc.assigned_to = row.get("assigned_to")
#             scheduling_tracker_doc.instructions_ = row.get("instructions_")
#             # Append the entire row to the "track" table fields
#             scheduling_tracker_doc.append("track", row)
#             scheduling_tracker_doc.insert()



import frappe
from frappe.model.document import Document

class MaintenanceScheduling(Document):
    pass

#SCHEDULING TO TRACKER AND CREATE A TRACKER TO SEND EMAIL ON SUBMIT >>>>>>>>>>>>>>>>>>>>>>

# @frappe.whitelist()
# def create_scheduling_tracker_documents(doctype, docname):
#     # Load the document
#     doc = frappe.get_doc(doctype, docname)

#     if doc.get("appointment"):
#         for row in doc.get("appointment"):
#             scheduling_tracker_doc = frappe.new_doc("Schedule Tracker")
#             scheduling_tracker_doc.sector_name = row.get("sector_name")
#             scheduling_tracker_doc.description_scheduling = row.get("description_scheduling")
#             scheduling_tracker_doc.assigned_to = row.get("assigned_to")
#             scheduling_tracker_doc.instructions_ = row.get("instructions_")
            
#             # Append the entire row to the "track" table fields
#             scheduling_tracker_doc.append("track", row)
#             scheduling_tracker_doc.insert()

#SCHEDULING TO TRACKER AND CREATE A TRACKER TO SEND EMAIL ON SAVE >>>>>>>>>>>>>>>>>>>>>>
@frappe.whitelist()
def create_scheduling_tracker_documents(doctype, docname):
    # Load the document
    doc = frappe.get_doc(doctype, docname)

    if doc.get("appointment"):
        for row in doc.get("appointment"):
            scheduling_tracker_doc = frappe.new_doc("Schedule Tracker")
            scheduling_tracker_doc.sector_name = row.get("sector_name")
            scheduling_tracker_doc.description_scheduling = row.get("description_scheduling")
            scheduling_tracker_doc.assigned_to = row.get("assigned_to")
            scheduling_tracker_doc.instructions_ = row.get("instructions_")
            
            # Append the entire row to the "track" table fields
            scheduling_tracker_doc.append("track", row)
            scheduling_tracker_doc.insert()



import frappe

@frappe.whitelist()
def btnfunction():
    # Your custom Python code here
    print("The button is working")
    return "The button is working"


















