import frappe
from frappe.permissions import add_permission, update_permission_property

# The documents table sits at permlevel 1 so a staff member's ID scans and licences are not
# readable by everyone who can open a User record, including the staff member themselves.
DOCUMENT_ROLES = ("System Manager",)


def execute():
	for role in DOCUMENT_ROLES:
		add_permission("User", role, 1)
		update_permission_property("User", role, 1, "read", 1)
		update_permission_property("User", role, 1, "write", 1)
