# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Referral(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.model.document import Document
		from frappe.types import DF

		clinic_session: DF.Data | None
		created_by: DF.Data | None
		created_on: DF.Datetime | None
		helpline_flag: DF.Check
		notes: DF.LongText | None
		patient: DF.Data
		patient_encounter: DF.Link | None
		priority: DF.Literal["Low", "Medium", "High"]
		project: DF.Link | None
		reason: DF.SmallText | None
		referral_by_source: DF.Data | None
		referral_followup: DF.Table[Document]
		referred_to: DF.Data | None
		referred_to_practitioner: DF.Link | None
		required_action_from: DF.Literal["None", "Programme", "Clinic"]
		status: DF.Literal["Pending", "In Progress", "Completed", "Lost"]
	# end: auto-generated types

	pass
