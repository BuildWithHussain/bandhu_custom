// Copyright (c) 2026, CMID and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Vehicle Usage Log", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Vehicle Usage Log', {
    odometer_end: function(frm) {
        if (frm.doc.odometer_start && frm.doc.odometer_end) {
            frm.set_value(
                'distance',
                frm.doc.odometer_end - frm.doc.odometer_start
            );
        }
    }
});
