# Copyright (c) 2022, Solufy and contributors
# For license information, please see license.txt

import frappe
from frappe import msgprint, _
from frappe.model.document import Document

class DirectShipping(Document):
	pass

def validate(self,cdt):
	for d in self.get('freight_order_line'):
		if d.pricing:
			if d.billing_on == "Volume":
				d.sale_price = d.volume * d.price
			else:
				d.sale_price = d.gross_weight * d.price
	test_d = frappe.db.get_value("Track Shipping Order",{'name1':self.name},'name')
	if test_d:
		test_doc = frappe.get_doc("Track Shipping Order",test_d)
		test_doc.source_location = self.loading_port
		test_doc.destination_location = self.discharging_port
		test_doc.transport_carriage = self.transport
		test_doc.status = self.workflow_state
		test_doc.save()
	else:
		vals = frappe.get_doc({
			"doctype": "Track Shipping Order",
			"name1":self.name,
			"source_location":self.loading_port,
			"destination_location":self.discharging_port,
			"transport_carriage":self.transport,
			"status":self.workflow_state
			})
		vals.save()