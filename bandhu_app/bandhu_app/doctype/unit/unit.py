# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Unit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		doctor: DF.Link | None
		driver: DF.Link | None
		nurse: DF.Link | None
		unit_name: DF.Data | None
	# end: auto-generated types

	pass
