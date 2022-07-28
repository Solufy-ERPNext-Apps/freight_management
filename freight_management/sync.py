import frappe


def install_missing_workflow_states():
	existing_states = frappe.db.get_all("Workflow State", pluck="name")
	required_states = set()

	for workflow_name in ["Revision", "Direct Shipping Workflow"]:
		workflow = frappe.get_doc("Workflow", workflow_name)
		for state in workflow.states:
			required_states.add(state.state)

	for state in required_states:
		if state not in existing_states:
			frappe.get_doc({
				"doctype": "Workflow State",
				"workflow_state_name": state
			}).insert(ignore_permissions=True)

	frappe.db.commit()


def after_sync():
	install_missing_workflow_states()
