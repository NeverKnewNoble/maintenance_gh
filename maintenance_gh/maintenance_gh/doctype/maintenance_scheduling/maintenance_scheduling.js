// Copyright (c) 2023, Larry-Noble and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Maintenance Scheduling', {
//     refresh: function(frm) {
// 		frm.add_custom_button(__('Reschedule This Issue'), function(){
// 		  frappe.msgprint(frm.doc.email);
// 		  frappe.set_route("Form", "Maintenance Rescheduling");
// 	  }, __("Reschedule"));
// 	}
// });

// frappe.ui.form.on('Maintenance Scheduling', {
//     refresh: function(frm) {
//         frm.add_custom_button(__('Reschedule This Issue'), function(){
//             frappe.new_doc("Maintenance Rescheduling", function(doc) {
//                 doc.linked_maintenance_scheduling = frm.doc.name;
//                 doc.sector = frm.doc.name; // Set 'sector' to the 'name' of the current document
//             });
//         }, __("Reschedule"));
//     }
// });


frappe.ui.form.on('Maintenance Scheduling', {
    refresh: function (frm) {
        frm.add_custom_button(__('Custom Button'), function () {
            frappe.call({
                method: 'maintenance_gh.maintenance_gh.doctype.maintenance_scheduling.maintenance_scheduling.btnfunction',
                args: {},
                callback: function (r) {
                    if (r.message) {
                        var maintenanceSchedulingID = frm.doc.name;  // Get the ID of the Maintenance Scheduling document
                        var url = `/app/maintenance-rescheduling/new-maintenance-rescheduling-1?sector=${maintenanceSchedulingID}`;
                        window.open(url, '_blank');
                    }
                }
            });
        });
    }
});





























  