# # Copyright (c) 2023, Larry-Noble and contributors
# # For license information, please see license.txt



# # PATRICK ANTEH CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>
# # import frappe
# # from frappe.model.document import Document


# # def maintenance(doc, event):
# #     if event == 'on_submit':

# #         maintenance_scheduling = frappe.new_doc('Maintenance Scheduling')

# #         maintenance_scheduling.ms_data = doc.issue_raised_by

# #         maintenance_scheduling.insert()
# #         maintenance_scheduling.submit()

    


# # class MaintenanceRequest(Document):
# #     def on_submit(self):
# #         maintenance(self, 'on_submit')



# PATRICK ADJEI CODE >>>>>>>>>>>>>>>>>>>>

# import frappe
# from frappe.model.document import Document

# class MaintenanceRequest(Document):
#     pass

# @frappe.whitelist()
# def create_scheduling_documents(doc):
#     # Deserialize the JSON string into a Python dictionary
#     doc = frappe.parse_json(doc)

#     if doc.get("sector"):
#         for row in doc.get("sector"):
#             scheduling_doc = frappe.new_doc("Maintenance Scheduling")
#             scheduling_doc.sector_name = row.get("sector_1")
#             scheduling_doc.description_scheduling = row.get("issue_description")
#             scheduling_doc.save()




# TRIAL 2 >>>>>>>>>>>>>>>>>>>

import frappe
from frappe.model.document import Document

#To pass the class
class MaintenanceRequest(Document):
    pass

@frappe.whitelist()
def create_scheduling_documents(doc):
    # Deserialize the JSON string into a Python dictionary
    doc = frappe.parse_json(doc)
    #To create new document in scheduling
    maintenance_scheduling = frappe.new_doc('Maintenance Scheduling')

    #To get and go through the sector and collect each row fields maping them to prev table fields
    if doc.get("sector"):
        for row in doc.get("sector"):
            maintenance_request_data = {
            "sector_name": row.get("sector_1"), 
            "description_scheduling":row.get("issue_description"),
        }
            #where we call scheduling table(new Table) with the method applied above.
            maintenance_scheduling.append("appointment", maintenance_request_data)
    #To save the scheduling document.
    maintenance_scheduling.save()
    

    










