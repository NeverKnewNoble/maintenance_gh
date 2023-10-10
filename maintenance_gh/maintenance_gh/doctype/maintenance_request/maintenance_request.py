# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class MaintenanceRequest(Document):
# 	pass


import frappe
from frappe.model.document import Document

def before_insert(doc, method):
    if not doc.get('issue_raised_by'):
        doc.issue_raised_by = frappe.session.user



class maintenance_request(Document):
    def on_submit(self):
        # Create a new terry Doctype document
        schedule_doc = frappe.new_doc("Maintenance Scheduling")
        # populate fields from prev doc"larry" to ne doc"terry"
        schedule_doc.sector_name = self.issue_raised_by  
        # Save the doc
        schedule_doc.save()
