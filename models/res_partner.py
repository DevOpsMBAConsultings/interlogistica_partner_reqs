from odoo import models, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('phone', 'street', 'is_company')
    def _check_interlogistica_mandatory_fields(self):
        for partner in self:
            # Solo aplica para contactos que no son empresas (is_company = False)
            if not partner.is_company:
                if not partner.phone:
                    raise ValidationError(_("El número de Teléfono es obligatorio."))
                if not partner.street:
                    raise ValidationError(_("La Dirección (Calle) es obligatoria."))
