# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2011 Vauxoo (<http://www.vauxoo.com>). All Rights Reserved
#    hbto@vauxoo.com / humbertoarocha@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	"name" : "Cálculo de Pago de Comisiones por producto pagado",
	"version" : "1",
	"author" : "Netquatro",
	"category" : "Generic Modules/Others",
	"website": "http://wiki.openerp.org.ve/",
	"description": '''
Cálculo de Pago de Comisiones por producto pagado
''',
	"depends" : ['account',
                'decimal_precision', 
                'baremo', 
                'account_voucher',],
	"init_xml" : [],
	"update_xml" : ['commission_report.xml','commission_view.xml'],
	"active": False,
	"installable": True
}
