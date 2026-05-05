# bandhu_app/bandhu_app/utils/custom_bandhu_id.py

import frappe


def set_bandhu_id(doc, method):
	# only set if empty
	if not doc.custom_bandhu_id:
		doc.custom_bandhu_id = frappe.model.naming.make_autoname("BMC-.#####")
