// Copyright (c) 2026, CMID and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Staff Log", {
// 	refresh(frm) {

// 	},
// });

// Auto-fill time check-in and check-out buttons
frappe.ui.form.on("Staff Log", {
	refresh: function (frm) {
		// Check In
		if (!frm.doc.check_in) {
			frm.add_custom_button("Check In", () => {
				frm.set_value("check_in", frappe.datetime.now_datetime());
				frm.save();
			});
		}

		// Check Out
		if (frm.doc.check_in && !frm.doc.check_out) {
			frm.add_custom_button("Check Out", () => {
				frm.set_value("check_out", frappe.datetime.now_datetime());
				frm.save();
			});
		}
	},
});
