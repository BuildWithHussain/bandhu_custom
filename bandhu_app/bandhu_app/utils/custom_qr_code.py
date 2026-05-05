import io

import frappe
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import HorizontalBarsDrawer


def make_qr_image(data: str) -> bytes:
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=10,
		border=4,
	)
	qr.add_data(data)
	qr.make(fit=True)

	img = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())

	output = io.BytesIO()
	img.save(output, format="PNG")
	return output.getvalue()


def generate_qr_code_file(doc, data: str, field_name="custom_qr_code"):
	qr_data = make_qr_image(data)

	file_doc = frappe.new_doc("File")
	file_doc.content = qr_data
	file_doc.attached_to_doctype = doc.doctype
	file_doc.attached_to_name = doc.name
	file_doc.attached_to_field = field_name
	file_doc.file_name = f"{doc.custom_bandhu_id}.png"
	file_doc.insert()

	return file_doc.file_url
