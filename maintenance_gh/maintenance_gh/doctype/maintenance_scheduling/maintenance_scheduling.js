// Copyright (c) 2023, Larry-Noble and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maintenance Scheduling', {
    refresh: function(frm) {
		frm.add_custom_button(__('Reschedule This Issue'), function(){
		  frappe.msgprint(frm.doc.email);
		  frappe.set_route("Form", "Maintenance Rescheduling");
	  }, __("Reschedule"));
	}
});
















  