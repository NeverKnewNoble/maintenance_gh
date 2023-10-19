// Copyright (c) 2023, Larry-Noble and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Maintenance Rescheduling', {
// 	// refresh: function(frm) {

// 	// }
// });

frappe.ui.form.on('Maintenance Rescheduling', {
    sector: function(frm) {
        if (frm.doc.sector) {
            frappe.call({
                method: 'maintenance_gh.maintenance_gh.doctype.maintenance_rescheduling.maintenance_rescheduling.populate_reappointment',
                args: { rescheduling_docname: frm.doc.sector },
                callback: function(r) {
                    if (!r.exc) {
                        frm.clear_table('reappointment');
                        for (var i = 0; i < r.message.length; i++) {
                            var row = frappe.model.add_child(frm.doc, 'reappointment', 'reappointment');
                            row.sector_name = r.message[i].sector_name;
                            row.description_scheduling = r.message[i].description_scheduling;
                            row.assigned_to = r.message[i].assigned_to;
                            row.instructions_ = r.message[i].instructions_;
                        }
                        frm.refresh_field('reappointment');
                    }
                }
            });
        }
    }
});
