# Copyright (c) 2026, CMID and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TestingFetchfrom(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		distr: DF.Data | None
		location: DF.Link | None
		lsg: DF.Data | None
		state: DF.Data | None
	# end: auto-generated types

	pass
