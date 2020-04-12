// Copyright (c) 2020, Aakvatech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Powerboard', {
	refresh: function(frm) {
		frm.add_custom_button(__("Show Powerboard"), () => frappe.set_route('powerboard', frm.doc.name));
	}
});
