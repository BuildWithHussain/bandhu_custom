# bandhu_app/bandhu_app/api.py

import frappe


@frappe.whitelist(allow_guest=True)
def get_patient_by_uid(uid: str):
    patient = frappe.get_all(
        "Patient",
        filters={"custom_bandhu_id": uid},
        fields=["name", "patient_name"]
    )

    if not patient:
        return {"error": "Patient not found"}

    return patient[0]
