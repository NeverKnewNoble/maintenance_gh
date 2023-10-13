// Copyright (c) 2023, Larry-Noble and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Maintenance Request', {
// 	// refresh: function(frm) {

// 	// }
// });

// frappe.ui.form.on('Maintenance Request', {
//     refresh: function(frm) {
//         if (!frm.doc.__islocal) {
//             // If the document is not new, don't make any changes
//             return;
//         }
//         if (frm.doc.__islocal) {
//             // Set the current date in the date_requested field
//             frm.set_value('date_requested', frappe.datetime.nowdate());
//         }

//         // Set the issue_raised_by field with the username of the logged-in user
//         frm.set_value('issue_raised_by', frappe.session.user);
//     }
// });


frappe.ui.form.on('Maintenance Request', {
    on_submit: function(frm) {
        frappe.call({
            method: 'maintenance_gh.maintenance_gh.doctype.maintenance_request.maintenance_request.create_scheduling_documents',
            args: { doc: frm.doc },
            callback: function(r) {
                if (!r.exc) {
                    frappe.msgprint('Maintenance Scheduling documents created successfully.');
                }
            }
        });
    },
    refresh: function(frm) {
        if (!frm.doc.__islocal) {
            // If the document is not new, don't make any changes
            return;
        }
        if (frm.doc.__islocal) {
            // Set the current date in the date_requested field
            frm.set_value('date_requested', frappe.datetime.nowdate());
        }

        // Set the issue_raised_by field with the username of the logged-in user
        frm.set_value('issue_raised_by', frappe.session.user);

        
    },

});
