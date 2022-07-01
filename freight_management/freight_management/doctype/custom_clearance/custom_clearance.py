# Copyright (c) 2022, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomClearance(Document):
	pass

def validate(self,cdt):
	if self.workflow_state == "Revision":	
		if self.revision_reason:
			cc_id = self.name
			cc_name = self.revision_reason	
			vals = frappe.get_doc({
				"doctype": "Custom Revision",
				"cc_id":cc_id,
				"revision_reason":cc_name
			})
			vals.insert()			
	
