# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MaintenanceRescheduling(Document):
    pass

@frappe.whitelist()
def populate_reappointment(rescheduling_docname):
    scheduling_doc = frappe.get_doc("Maintenance Scheduling", rescheduling_docname)
    reappointment_data = []

    # for row in scheduling_doc.get("appointment"):

    #     reappointment_data.append({
    #         "sector_name": row.get("sector_name"),
    #         "description_scheduling": row.get("description_scheduling"),
    #         "assigned_to": row.get("assigned_to"),
    #         "instructions_": row.get("instructions_")
    #     })

    for row in scheduling_doc.get("appointment"):
        scheduling_tracker_doc = frappe.new_doc("Reschedule Tracker")
        scheduling_tracker_doc.append("track", row)
        scheduling_tracker_doc.insert()

        reappointment_data.append({
            "sector_name": row.get("sector_name"),
            "description_scheduling": row.get("description_scheduling"),
            "assigned_to": row.get("assigned_to"),
            "instructions_": row.get("instructions_")
        })

     

    return reappointment_data