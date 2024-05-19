from odoo import fields, models,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_name = fields.Char(string='Employee Name',tracking=1 )
    has_group = fields.Char(string='HAS Group')
    company_name = fields.Char(string='Company Name')
    email = fields.Char(string='Email')
    contact_number = fields.Char(string='Contact Number')
    designation = fields.Char(string='Designation')
    onboarding = fields.Date(string='Onboarding')
    follow_up = fields.Date(string='Follow Up')
    request_meeting = fields.Boolean(string='Request Meeting')
    action = fields.Char(string='Action')
    sorting = fields.Integer(string='Sorting')
    forecasting = fields.Char(string='Forecasting')
    pipelines_leads = fields.Char(string='Pipelines Leads')
    quotation = fields.Char(string='Quotation')
    created_by = fields.Many2one('res.users', string='Created By', compute='_compute_created_by', store=True)



    @api.depends('create_uid')
    def _compute_created_by(self):
        for record in self:
            record.created_by = record.create_uid

