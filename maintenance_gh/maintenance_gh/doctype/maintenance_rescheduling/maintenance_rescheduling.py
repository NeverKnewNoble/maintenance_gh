# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MaintenanceRescheduling(Document):
	pass

def populate_sector_data(doc, method):
    if doc.selected_maintenance_scheduling:
        # Get the selected "Maintenance Scheduling" document
        maintenance_scheduling_doc = frappe.get_doc("Maintenance Scheduling", doc.selected_maintenance_scheduling)

        # Clear existing rows in the "sector_data" table
        doc.sector_data = []

        # Populate the "sector_data" table with data from the selected document
        for row in maintenance_scheduling_doc.get("appointment"):
            sector_data = doc.append("reappointment", {})
            sector_data.sector_name = row.get("sector_name")
            sector_data.description_scheduling = row.get("description_scheduling")

    # Save the "Maintenance Rescheduling" document
    doc.save()
