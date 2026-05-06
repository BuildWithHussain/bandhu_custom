# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ReferralFollowup(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		followup_date: DF.Date | None
		next_followup_date: DF.Date | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		status_update: DF.Literal["No Response", "Visited Hospital", "Under Treatment", "Completed"]
		summary: DF.SmallText | None
	# end: auto-generated types

	pass
