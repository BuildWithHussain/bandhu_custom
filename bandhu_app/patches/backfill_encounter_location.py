import frappe

# custom_lsg, custom_district and custom_state on Patient Encounter all fetch from
# custom_location, and nothing had ever set that link -- so every visit recorded before this
# patch carries three empty fields the scope of work asks the software to capture by itself.
LOCATION_FIELDS = ("lsg", "district", "state")


def execute():
	encounters = frappe.get_all(
		"Patient Encounter",
		filters={"custom_location": ["is", "not set"], "custom_clinic_session": ["is", "set"]},
		fields=["name", "custom_clinic_session"],
	)
	if not encounters:
		return

	sessions = {row.custom_clinic_session for row in encounters}
	site_by_session = dict(
		frappe.get_all(
			"Bandhu Clinic Session",
			filters={"name": ["in", list(sessions)]},
			fields=["name", "site"],
			as_list=True,
		)
	)
	location_by_site = dict(
		frappe.get_all(
			"Site",
			filters={"name": ["in", list({site for site in site_by_session.values() if site})]},
			fields=["name", "location"],
			as_list=True,
		)
	)
	details_by_location = {
		row.name: row
		for row in frappe.get_all(
			"Bandhu Location",
			filters={"name": ["in", list({loc for loc in location_by_site.values() if loc})]},
			fields=["name", *LOCATION_FIELDS],
		)
	}

	for row in encounters:
		location = location_by_site.get(site_by_session.get(row.custom_clinic_session))
		details = details_by_location.get(location)
		if not details:
			continue

		# db.set_value, not a save: these are historical visits, some of them completed, and
		# re-saving would re-run the workflow hooks on records nobody is touching.
		frappe.db.set_value(
			"Patient Encounter",
			row.name,
			{
				"custom_location": location,
				**{f"custom_{field}": details.get(field) for field in LOCATION_FIELDS},
			},
			update_modified=False,
		)
