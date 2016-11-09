# -*- coding: utf-8 -*-

from openerp import models, fields, api

class inside_audit(models.Model):
    _name = 'inside_audit'      
    _inherit = 'audit.audit'         

    name = fields.Char(require=True,string="名称")
    
    state=fields.Selection([
    ('information',u'了解内部审计工作'),
    ('decide',u'决定使用内部审计人员工作'),
    ('evaluation',u'评估使用的内部审计的工作'),
    ],default='information')
    active=fields.Boolean(default=True,string='激活')
    
    information=fields.Html(string='内部审计的基本情况')
    yesorno=fields.Boolean(string='是否有内部审计工作',default=True)
    relativity=fields.Boolean(string='内部审计工作是否与本项目审计相关',default=True)
    
    #内部审计人员的工作是否足以实现审计目的
    objectivity=fields.Boolean(string='内部审计工作是否具有客观性',default=True)
    objectivity_description=fields.Html(string='内部审计工作具有客观性说明')
    ability=fields.Boolean(string='内部审计工作人员是否具有职业胜任能力',default=True)
    ability_description=fields.Html(string='内部审计工作人员具有职业胜任能力说明')
    attention=fields.Boolean(string='内部审计工作人员执行内部审计工作时是否应有的关注',default=True)
    attention_description=fields.Html(string='内部审计工作人员执行内部审计工作时应有的关注的说明')
    communication=fields.Boolean(string='与内部审计工作人员是否可进行有效沟通',default=True)
    communication_description=fields.Html(string='与内部审计工作人员进行沟通的说明')
    
    ##内部审计人员的工作对审计程序的影响
    affect=fields.Html(string='说明内部审计人员已经执行或者拟执行的审计程序的性质与范围')
    rmm=fields.Html(string='评估的特定交易,余额与披露的认定层次的重大错报风险说明')
    subjectivity=fields.Html(string='内部审计人员对审计证据评价的主观性说明')    
    accept=fields.Boolean(string='确定利用内部审计人员的工作',default=True)
    
    #评价内部审计工作
    abilitytwo=fields.Boolean(string='内部审计工作人员经充分技术培训且精通业务',default=True)
    abilitytwo_description=fields.Html(string='内部审计工作人员经充分技术培训且精通业务的说明')
    monitor=fields.Boolean(string='内部审计工作人员工作经适当监督,复核与记录',default=True)
    monitor_description=fields.Html(string='内部审计工作人员工作经适当监督,复核与记录的说明')
    evidence=fields.Boolean(string='内部审计工作证据的充分适当,结论合理适当,与内部审计报告结论一致',default=True)
    evidence_description=fields.Html(string='内部审计工作证据的充分性适当性,结论合理适当,与与内部审计报告结论一致的说明')
    conclusion=fields.Boolean(string='内部审计人员工作证据与结论的是否可接受为审计证据',default=True)
    conclusion_description=fields.Html(string='内部审计工作证据与结论及其对审计程序性质,时间与范围的影响')
    attachment=fields.Binary(string="评价工作的相关附件")

    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The inside audit title must be unique"),
    ]

#重写复制方法,使复制选项可用
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(inside_audit, self).copy(default)            
    
    @api.multi
    def action_decide(self):
        self.state='decide'    
        
    @api.multi
    def action_evaluation(self):
        self.state='evaluation'    
        
    @api.multi
    def action_information(self):
        self.state='information'                    
