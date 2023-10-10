# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt 
import frappe
from frappe.model.document import Document

class Larry(Document):
    def after_submit(self):
        # Create a new Derrick Doctype document
        terry_doc = frappe.new_doc("Terry")
        terry_doc.terry_text = self.larry_text  # Populate derrick_text
        terry_doc.save()
