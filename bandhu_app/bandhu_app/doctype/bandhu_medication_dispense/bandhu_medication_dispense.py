# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BandhuMedicationDispense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from bandhu_app.bandhu_app.doctype.prescription.prescription import Prescription

		clinic_session: DF.Data | None
		dispensed_by: DF.Link | None
		encounter: DF.Link | None
		instructions: DF.SmallText | None
		nurse_name: DF.Data | None
		patient: DF.Data | None
		prescription_ref: DF.Link | None
		project: DF.Data | None
		source: DF.Literal["In-house", "External"]
		status: DF.Literal["Pending", "Dispensed"]
		table_pbtr: DF.Table[Prescription]
	# end: auto-generated types

	pass
