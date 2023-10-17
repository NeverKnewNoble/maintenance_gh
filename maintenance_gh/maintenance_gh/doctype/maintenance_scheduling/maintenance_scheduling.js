// Copyright (c) 2023, Larry-Noble and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Maintenance Scheduling', {
//     on_submit: function(frm) {
//         frappe.call({
//             method: 'maintenance_gh.maintenance_gh.doctype.maintenance_scheduling.maintenance_scheduling.create_scheduling_tracker_documents',
//             args: { doc: frm.doc },
//             callback: function(r) {
//                 if (!r.exc) {
//                     frappe.msgprint('Maintenance Scheduling Tracker documents created successfully.');
//                 }
//             }
//         });
//     },
//     refresh: function(frm) {
// 		frm.add_custom_button(__('Reschedule This Issue'), function(){
// 		  frappe.msgprint(frm.doc.email);
// 		  frappe.set_route("Form", "Maintenance Rescheduling");
// 	  }, __("Reschedule"));
// 	}
// });



frappe.ui.form.on('Maintenance Scheduling', {
    on_submit: function(frm) {
        frappe.call({
            method: 'maintenance_gh.maintenance_gh.doctype.maintenance_scheduling.maintenance_scheduling.create_scheduling_tracker_documents',
            args: { doc: frm.doc },
            callback: function(r) {
                if (!r.exc) {
                    frappe.msgprint('Maintenance Scheduling Tracker documents created successfully.');
                }
            }
        });
    },
    refresh: function(frm) {
		frm.add_custom_button(__('Reschedule This Issue'), function(){
		  frappe.msgprint(frm.doc.email);
		  frappe.set_route("Form", "Maintenance Rescheduling");
	  }, __("Reschedule"));
	}
});




  