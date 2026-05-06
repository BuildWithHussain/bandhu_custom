// Copyright (c) 2026, CMID and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Vehicle Refuel Log", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Vehicle Refuel Log', {

    quantity: calculate_amount,
    rate: calculate_amount,

    validate: function(frm) {
        calculate_amount(frm);
    }
});

function calculate_amount(frm) {
    if (frm.doc.quantity && frm.doc.rate) {
        let amount = frm.doc.quantity * frm.doc.rate;
        frm.set_value('amount', amount);
    }
}