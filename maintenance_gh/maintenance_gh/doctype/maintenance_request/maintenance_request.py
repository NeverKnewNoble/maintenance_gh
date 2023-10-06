# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class MaintenanceRequest(Document):
# 	pass

import frappe

def before_insert(doc, method):
    if not doc.get('issue_raised_by'):
        doc.issue_raised_by = frappe.session.user