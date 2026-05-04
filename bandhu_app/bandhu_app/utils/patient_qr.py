
import frappe

from bandhu_app.bandhu_app.utils.custom_qr_code import generate_qr_code_file


def create_patient_qr(doc, method):
    # avoid duplicate generation
    if doc.custom_qr_code:
        return

    if not doc.custom_bandhu_id:
        return

    file_url = generate_qr_code_file(
        doc=doc,
        data=f"{frappe.utils.get_url()}/api/method/bandhu_app.api.get_patient_by_uid?uid={doc.custom_bandhu_id}",
        field_name="custom_qr_code"
    )

    # update field
    doc.db_set("custom_qr_code", file_url)
