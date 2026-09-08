import frappe

# Every board re-reads its own queues when this lands, so the push carries the camp name and
# nothing else. It goes to the site room -- every System User receives it, not only the three
# people running the camp -- which is why no patient data travels with it.
BOARD_UPDATE_EVENT = "bandhu_board_update"


def publish_board_update(clinic_session: str | None) -> None:
	if not clinic_session:
		return

	frappe.publish_realtime(
		BOARD_UPDATE_EVENT,
		# The person who made the change has already refreshed their own board by the time this
		# lands; without the actor they would re-render a second time and lose their scroll place.
		{"clinic_session": clinic_session, "actor": frappe.session.user},
		# Without after_commit a board re-reads the queue before the write it is reacting to is
		# visible, and paints the state the staff just changed away from.
		after_commit=True,
	)


def broadcast_encounter_change(doc, method=None) -> None:
	publish_board_update(doc.custom_clinic_session)
