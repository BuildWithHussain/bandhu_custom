// Copyright (c) 2026, CMID and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Bandhu Clinic Session", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on('Bandhu Clinic Session', {
// 	refresh(frm) {
// 		// your code here
// 	}
// })

frappe.ui.form.on('Bandhu Clinic Session', {

    refresh: function(frm) {

        // START BUTTON
        if (frm.doc.status === "Planned") {
            frm.add_custom_button("Start Session", async () => {

                // basic guard
                if (!frm.doc.clinic || !frm.doc.date) {
                    frappe.msgprint("Please set Clinic and Date before starting.");
                    return;
                }

                frm.set_value("status", "In Progress");
                frm.set_value("start_time", frappe.datetime.now_datetime());
                await frm.save();

                frappe.show_alert({message: "Session Started", indicator: "green"});
            });
        }

        // END BUTTON
        if (frm.doc.status === "In Progress") {
            frm.add_custom_button("End Session", async () => {

                // optional safety checks
                // (keep light for now)
                frm.set_value("status", "Completed");
                frm.set_value("end_time", frappe.datetime.now_datetime());
                await frm.save();

                frappe.show_alert({message: "Session Completed", indicator: "blue"});
            });
        }

    }
});
