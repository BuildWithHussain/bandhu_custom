import frappe


def execute():
	"""Patient carried two fields both labelled "Clinic ID": custom_bandhu_id, which holds every
	issued ID, and custom_clinic_id, which was empty on every patient. One label on two fields
	means a print format, report column or export picks the blank one half the time."""
	field_name = "Patient-custom_clinic_id"

	frappe.clear_cache(doctype="Patient")
	column_exists = frappe.db.has_column("Patient", "custom_clinic_id")

	# Re-runs on restores and on a migrate that already applied this, so it has to cope with the
	# column being gone while the Custom Field record is still there, and the other way round.
	if column_exists and frappe.db.count("Patient", {"custom_clinic_id": ["is", "set"]}):
		# Never drop a column that turned out to hold something. If this ever fires, the field
		# earned its place and the duplicate label has to be settled by renaming instead.
		frappe.log_error(title="custom_clinic_id holds data; not removed")
		return

	if frappe.db.exists("Custom Field", field_name):
		frappe.delete_doc("Custom Field", field_name, ignore_permissions=True)

	# Frappe's schema sync only ever adds columns, so deleting the Custom Field alone leaves the
	# column behind. has_column reads a cached column list, hence the clear on both sides.
	if column_exists:
		frappe.db.sql_ddl("alter table `tabPatient` drop column `custom_clinic_id`")
		frappe.clear_cache(doctype="Patient")
