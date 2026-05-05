# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PatientQueue(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		clinic_session: DF.Data | None
		completed_on: DF.Datetime | None
		created_on: DF.Autocomplete | None
		current_stage: DF.Literal[
			"Waiting", "With Doctor", "With Nurse (Test)", "With Nurse (Medicine)", "Completed"
		]
		encounter: DF.Link | None
		handled_by: DF.Link | None
		last_updated: DF.Autocomplete | None
		patient: DF.Data | None
		status: DF.Literal["Active", "Done"]
	# end: auto-generated types

	pass
