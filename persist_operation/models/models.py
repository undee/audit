# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from openerp import models, fields, api

class persist_operation(models.Model):
    _name = 'persist_operation'
    _inherit = 'audit.audit'              

    
    name = fields.Char(require=True,string=u"名称")
    active=fields.Boolean(default=True)
    state=fields.Selection([
        ('executory', "Executory"),
        ('done','Done'),
    ], default='executory')
    preliminary_estimate=fields.Boolean(require=True,string=u"管理层是否就持续经营能力进行初步评估")
    preliminary_estimate_information=fields.Html(string=u"管理层就持续经营能力进行初步评估信息")
    
    discuss1=fields.Html(string=u"与管理层讨论持续经营能力")
    exist_case_affect_persist_operation=fields.Boolean(string=u"管理层是否识别出对持续经营能力产生重大疑虑的事项或情况")
    case_affect_persist_operation=fields.Html(string=u"管理层识别出对持续经营能力产生重大疑虑的事项或情况")
    reply_to_case=fields.Html(string=u"与管理层就其识别出对持续经营能力产生重大疑虑的事项或情况的应对计划进行讨论")
    
    cpa_evaluate_period_begin=fields.Date()
    cpa_evaluate_period_end=fields.Date()
    
    manager_evaluate_period_begin=fields.Date()
    manager_evaluate_period_end=fields.Date()    
    
    evaluate_period_same=fields.Boolean(string=u"CPA评价期间与管理层对持续经营能力的评估期间是否一致",compute="_evaluate_period_same")
    
    evaluate_period_more_than=fields.Boolean(string=u"管理层评价持续经营能力的涵盖期间是否大于12个月",compute="_evaluate_period_more_than",default=True)
    
    manager_evaluate_information=fields.Html(string=u'管理层所评估的信息')
    cpa_observe_information=fields.Html(string=u'CPA注意到的信息')
    manager_evaluate_information_enough=fields.Boolean(string=u"管理层所评估的信息是否包括CPA注意到的信息",default=True)
    
    exceed_period_if=fields.Boolean(string=u"询问管理层是否存在超出管理层评估期间,可能导致对持续经营能力产生重大疑虑的事项与情况.",default=False)
    exceed_period=fields.Html(string=u'对超出管理层评估期间事项与情况的询问')    
    
    identification=fields.Boolean(string=u"CPA是否识别出可能导致对持续经营能力产生重大疑虑的事项或情况 ",default=False)
    # 未来被设置为One2many,数据源自其他审计程序,如分析程序与细节测试
    identify_information=fields.Html(string=u"CPA识别出可能导致对持续经营能力产生重大疑虑的事项或情况")
    
    reply_method=fields.Html(string=u"进一步审计程序",
                             default=u"""<ul>
                             <li class="basic">提请管理层作出评估</li>
                             <li class="basic">评估应对计划</li>
                             <li class="basic">评价现金流量预测的基础数据以及现金流量预测的假设</li>
                             <li class="basic">评估后事实或信息的评价</li>
                             <li class="basic">获取应对计划及可行性的声明书</li>
                             </ul>    
    """)
    
    evidence=fields.Selection([
        ('negation',u'管理层在财务报表中运用持续经营假设是不适当的,或者管理层运用持续经营假设适合具体情况,但是没有充分描述主要事项或情况及其应对措施'),
        ('reserve',u'管理层运用持续经营假设适合具体情况,但是没有充分描述可能导致对持续经营能力产生重大疑惑的主要事项或情况及其应对措施'),
        ('emphasize',u'管理层运用持续经营假设适合具体情况,并且已经充分描述可能导致对持续经营能力产生重大疑惑的主要事项或情况及其应对措施'),
        ('standard',u'管理层运用持续经营假设适合具体情况,CPA未识别出可能导致对持续经营能力产生重大疑惑的主要事项或情况')
        ])
    
    draft_report_type=fields.Char(string='拟出具报告类型',compute="_draft_report_type")
        
    delay_report_if=fields.Boolean(u"是否存在严重拖延报告的情况",default=False)
    delay_report_reason=fields.Text(u"严重拖延报告的原因")
    delay_report_relativity=fields.Boolean(u'严重拖延报告是否涉及对持续经营的评估',default=True)
    
    communicate=fields.Html(string=u'与治理层沟通',
                             default=u"""<ul>
                             <li class="basic">构成重大不确定性的事项或情况</li>
                             <li class="basic">财务报表中应用持续经营假设的适当性</li>
                             <li class="basic">财务报表中的相关披露充分</li>
                             </ul>        
    """)  
    

    branch_manager_with_discuss=fields.Html(string=u"与管理层讨论其拟运用的持续经营假设的基础")
    branch_manager_inquiry=fields.Boolean(string=u"是否存在可能导致对持续经营能力产生重大疑虑的事项或情况")
#     branch_request=fields.Boolean(string=u"是否向管理层提请作出持续经营能力的评估")    
    
    
    @api.depends('cpa_evaluate_period_begin', 'manager_evaluate_period_begin','cpa_evaluate_period_end','manager_evaluate_period_end')
    def _evaluate_period_same(self):    
        if self.cpa_evaluate_period_begin!=self.manager_evaluate_period_begin:
            evaluate_period_same=False
        if self.cpa_evaluate_period_end!=self.manager_evaluate_period_end:
            evaluate_period_same=False
     
            
    @api.depends('manager_evaluate_period_begin', 'manager_evaluate_period_end')
    def _evaluate_period_more_than(self):    
        pass

    @api.depends('evidence')    
    def _draft_report_type(self):
        if self.evidence=='negation':
            self.draft_report_type=u'否定意见'
        elif self.evidence=='reserve':
            self.draft_report_type=u'保留意见'
        elif self.evidence=='emphasize':
            self.draft_report_type=u'带强调事项的标准意见'            
        elif self.evidence=='standard':
            self.draft_report_type=u'标准意见'        
            
    @api.multi
    def action_done(self):
        self.state='done'
        
    @api.multi
    def action_executory(self):
        self.state='executory'            
            
        
        
