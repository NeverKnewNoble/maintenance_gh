# Copyright (c) 2023, Larry-Noble and contributors
# For license information, please see license.txt



# Patrick code>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import frappe
# from frappe.model.document import Document



# def maintenance(doc, event):
#     if event == 'on_submit':

#         maintenance_scheduling = frappe.new_doc('Maintenance Scheduling')

#         maintenance_scheduling.ms_data = doc.issue_raised_by

#         maintenance_scheduling.insert()
#         maintenance_scheduling.submit()

    


# class MaintenanceRequest(Document):
#     def on_submit(self):
#         maintenance(self, 'on_submit')
        


# trial 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import frappe
from frappe.model.document import Document
from frappe import get_doc, core



def maintenance(doc, event):
    if event == 'on_submit':

        maintenance_scheduling = frappe.new_doc('Maintenance Scheduling')

        source_doc = get_doc('Maintenance Request', MaintenanceRequest)
        source_child_table = source_doc.sector
        
        target_doc = get_doc('Maintenance Scheduling',maintenance_scheduling)

        target_doc.sector_1 = source_child_table

        
        maintenance_scheduling.insert()
        maintenance_scheduling.submit()

    


class MaintenanceRequest(Document):
    def on_submit(self):
        maintenance(self, 'on_submit')





# Almost there>>>>>>>>>>>>>>>>>>>>
# import frappe
# from frappe.model.document import Document
# from frappe import get_doc, core



# def maintenance(doc, event):
#     if event == 'on_submit':

#         maintenance_scheduling = frappe.new_doc('Maintenance Scheduling')

#         source_doc = get_doc('Maintenance Request', MaintenanceRequest)
#         source_child_table = source_doc.sector
        
#         target_doc = get_doc('Maintenance Scheduling',maintenance_scheduling)

#         target_doc.sector_1 = source_child_table
#         target_doc.issue_description = source_child_table

#         maintenance_scheduling.insert()
#         maintenance_scheduling.submit()

    


# class MaintenanceRequest(Document):
#     def on_submit(self):
#         maintenance(self, 'on_submit')







