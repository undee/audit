# -*- coding: utf-8 -*-

from openerp import models, fields, api

class expertise(models.Model):
    _name = 'expertise.expertise'
    _inherit = 'audit.audit'     


    name = fields.Char()
    active=fields.Boolean(default=True)
    state=fields.Selection([
        ('draft', "Bring forward"),
        ('waite', "Waiting decise"),
        ('agreement', "Agreemen"),
        ('evaluation','Result evaluation'),
        ('report','Report'),
        ('done','Done'),
    ], default='draft')
    #由审计员提出利用专家的工作
    reason=fields.Text(string=u'需要利用专家的工作时,填写提出的理由',help=u'如果在执行审计程序过程中遇到会计审计领域外的专长(专门的技能知识与能力)对获取审计证据是必要的情况,根据CAS1421号准则可以向项目负责人提出利用专家的工作来获取必要的审计证据.',translate=True)
    
    #项目负责人评估请求以决定是否利用专家的工作
    nature_of_matter=fields.Text(string=u'利用专家工作事项的性质',help='')
    # todo:这里也可以使用一个函数获取定义的重大错报风险程度,可以是百分比形式的浮点数
    RMM=fields.Selection([
        ('high', "High"),
        ('medium', "Medium"),
        ('low', "Low"),
    ], default='high',require=True,translate=True)
    IWE=fields.Selection([
        ('high', "High"),
        ('medium', "Medium"),
        ('low', "Low"),
    ], default='high',require=True,translate=True)
    understand=fields.Html(string='',help='')
    rule=fields.Boolean(string='',help='',default=True)
    
    #项目负责人决定利用专家进行工作,与专家达到一致意见,签订书面协议
    
    #协议扫描后以PDF文件形式上传
    agreement_done=fields.Binary(string='agreement',attachment=True)
    agreement=fields.Html(string='',help=u'',require=True,default=u"""
    <h3>按照下面内容与专家进行沟通,形成书面协议</h3>
    <ul class="">
    <li class="basic"><div class="nodecontent">专家的工作性质,范围与要求</div></li>
    <li class="basic"><div class="nodecontent">项目负责人与专家各自的角色与责任</div></li>
    <li class="basic"><div class="nodecontent">沟通的性质时间与范围,包括报告的形式</div></li>
    <li class="basic"><div class="nodecontent">保密要求</div></li>
    </ul>    
    """)
    
    #专家的工作报告收到后以PDF文件形式上传
    expert_result=fields.Binary(string='agreement report',attachment=True)
    
    #评估专家的工作结果,可以
    relativity=fields.Boolean(string=u'与审计事项相关')
    reliability=fields.Boolean(string=u'作为审计证据可靠性可以接受')
    evidence_consistency=fields.Boolean(string=u'证据一致性')
    evidence_method_hypothesis=fields.Boolean(string=u'采用的重要假设与方法是否与审计事项相关,是否合理')
    original_data=fields.Boolean(string=u'专家的工作中使用的原始数据是完整性可靠性相关性是否可以接受')
    
#     报告类型可以通过其他模块的执行结果获取
#     report_type=fields.Char()
#     report_words=fields.Char(compute="_get_words")
#      
#     @api.depends("report_type")
#     def _get_words(self):
#         self.report_words=self.report_type

#  原型只是简单提供几种选择    
    report_type=fields.Selection([
          ('unreserve','Unreserve without mention'),
          ('unreserveLaws','Unreserve but laws demand mention'),
          ('reserve','Reserve without mention'),
          ('reservemention','Reserve and mention'),                                      
    ],
     string=u'是否在审计报告中提及专家的工作',
     default='unreserve',
     translate=True
    )
    report_words=fields.Char(compute='_get_report_type',translate=True)
     
 
    @api.depends("report_type")
    def _get_report_type(self):        
        if self.report_type:
            if self.report_type=='unreserve':
                self.report_words=u'无保留意见中不应提及专家的工作'
            elif self.report_type=='unreserveLaws':
                self.report_words=u'无保留意见中因法律法规的规定要求提及专家的工作,审计意见的措词要注意'
            elif self.report_type=='reservemention':
                self.report_words=u'保留意见中提及了专家的工作,审计意见的措词要注意'
            elif self.report_type=='reserve':
                self.report_words=u'保留意见中不应提及专家的工作'    
            else:
                self.report_words=u'不适用'   
            
    @api.multi
    def action_accept(self):
        self.state='waite'
        
    @api.multi
    def action_agreement(self):
        self.state='agreement'
        
    @api.multi
    def action_evaluation(self):
        self.state='evaluation'   
        
    @api.multi
    def action_report(self):
        self.state='report'  
        
    @api.multi
    def action_done(self):
        self.state='done'  
        
#名称唯一性

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The expertise work title must be unique"),
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
        return super(expertise, self).copy(default)        
                
        
                    
        
        