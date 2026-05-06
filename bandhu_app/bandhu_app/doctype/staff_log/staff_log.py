# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StaffLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		check_in: DF.Datetime
		check_out: DF.Datetime
		clinic_session: DF.Link
		user: DF.Link
	# end: auto-generated types

	pass
