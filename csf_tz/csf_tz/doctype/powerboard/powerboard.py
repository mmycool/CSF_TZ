# -*- coding: utf-8 -*-
# Copyright (c) 2020, Aakvatech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe

class Powerboard(Document):
	def on_update(self):
		if self.is_default:
			# make all other dashboards non-default
			frappe.db.sql('''update
				tabPowerboard set is_default = 0 where name != %s''', self.name)
