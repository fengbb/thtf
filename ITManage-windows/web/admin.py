#-*- coding:utf-8 -*-
##定义使用utf-8编码
#导入django admin，导入后就可以注册使用了
from django.contrib import admin
#使用django表单，需要创建forms.py
from django import forms
# Register your models here.
#导入web下定义的models，数据库定义，
from web import models
##这些都是在模板中使用的
from django.shortcuts import render_to_response,render,HttpResponse
##django.contrib.admin.views.decorators 中的 staff_member_required 修饰器。该修饰器与第 12 章中讨论的 login_required 类似，但它还检查所指定的用户是否标记为内部人员，以决定是否允许他访问管理界面。
##该修饰器保护所有内容的管理视图，并使得视图的身份验证逻辑匹配管理界面的其它部分
from django.contrib.admin.views.decorators import staff_member_required
##使用url
from django.conf.urls import patterns,include,url
#has_add_permission has_delete_permission 方法，可以定制 model 的修改删除行为。
#重写 get_readonly_fields 方法，可以针对某些字段设置为只读而不能修改。
#再重写 save_model可以修改 model 保存时候的一些行为。
#重写 change_view方法，可以修改 修改 model 时候的行为
#总而言之，如果需要自定义 django 的 admin 又不想更改 django 源码，就只能重写 admin.ModelAdmin 这个 class 的一些方法接口。配合返回的 queryset 和 permission，大部分业务需求都能完成。
class HostAdmin(admin.ModelAdmin):
    #前面定义的models在admin管理界面是不显示的，只有在着定义并且注册，才可以在admin界面显示
    ##search_fields定义搜索的时候可以查找字段
    #而search_fields会在页面顶端加入一个搜索栏
    search_fields = ('hostname','ip_addr')
    ##list_display定义显示字段，models中定义的字段可以在着选择那些显示
    #它是一个字段名称的元组，用于列表显示
    list_display = ('hostname','ip_addr','port','system_type','enabled')
##设置子对象并设计成内联编辑,就是hosts和bindhost有关联，bindhost中的hostname要在hosts中存在
class BindHostInline(admin.TabularInline):
    model = models.BindHosts.host_group.through
    readonly_fields = ['hostname']
    def hostname(self,instance):
        print (dir(instance))
        return '%s(%s)' % (instance.bindhosts.host.hostname,instance.bindhosts.host.ip_addr)
    hostname.short_description = 'row name'
class HostUserAdmin(admin.ModelAdmin):
    list_display = ('auth_method','username')
class BindHostAdmin(admin.ModelAdmin):
    #get_groups返回group name
    list_display = ('host','host_user','get_groups')
    list_filter = ('host','host_user','host_group')
    #当遇到many-to-many的多选的字段类型时，Django自动提供上图中的选择方式，不过还可以
    #选择用其它方式来进行多选，这种方式更加直观，不过只能作用于many-to-many的多选字段，
    #不能应用于foreignkey字段。
    #就是图标选择这种方式
    filter_horizontal = ('host_group',)
    #在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    raw_id_fields = ("host",'host_user')
    def get_urls(self):
        urls = super(BindHostAdmin,self).get_urls()
        my_urls = patterns("",
                           url(r"^multi_add/$",self.multi_add)
                           )
        return my_urls + urls
    def multi_add(self,request):
        if request.user.is_superuser:
            import admin_custom_view
            err = {}
            result = None
            chosen_data = {}
            if request.method == 'POST':
                print(request.POST)
                form_obj = admin_custom_view.BindHostsMultiHandle(request)
                if form_obj.is_valid():
                    form_obj.save()
                    result = form_obj.result
                else:
                    err = form_obj.err_dic
                chosen_data = form_obj.clean_date
            host_users = models.HostUsers.objects.all()
            hosts = models.Hosts.objects.all()
            host_group = models.HostGroups.objects.all()
            return render(request,'admin/web/BindHosts/multi_add.html',{
                'user':request.user,
                'host_users':host_users,
                'host_groups':host_group,
                'hosts':hosts,
                'err':err,
                'chosen_data':chosen_data,
                'result':result
            })
        else:
            return HttpResponse("Only superuser can access this page!")
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #Inline 类允许 admin 用户在单个页面编辑或添加多个相关模型
    inlines = [
        BindHostInline
    ]
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','department','valid_begin_time','valid_end_time')
    filter_horizontal = ('host_groups','bind_hosts')
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id','session','user','host','action_type','cmd','date')
    list_filter = ('session','user','host','action_type','date')
    search_fields = ['user__user__username','host__host__hostname','host__host__ip_addr','cmd']
    #django的admin后台管理系统中自带了一个批量删除所选对象的action
    #我们还可以添加自定义的action来实现其它类似的功能，如批量修改某个字段的功能
    actions = ['make_published']
    def get_actions(self, request):
        actions = super(AuditLogAdmin,self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    def make_published(self,request,queryset):
        rows_deleted = models.AuditLog.objects.all()
        print ('--row:',rows_deleted)
        message_bit = "1 story was"
        self.message_user(request,"%s successfully marked as published." % message_bit)
    ##这里的短描述是action下拉框中显示的描述
    make_published.short_description = '删除3个月以前的审计日志'
    def suit_row_attributes(self,obj,request):
        css_class = {
            1: 'success',
            2: 'warning',
            5: 'error',
        }.get(obj.action_type)
        if css_class:
            return {'class':css_class,'data': obj.action_type}
    def has_add_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    #不同权限的可以编辑不同的内容，可以通过get_readonly_fileds()来添加字段只读权限。
    readonly_fields = models.AuditLog._meta.get_all_field_names()
class TaskLogAdmin(admin.ModelAdmin):
    list_display =  ('id','start_time','end_time','task_type','user','cmd','total_task','success_task','failed_task','unknown_task','expire_time')
    list_filter = ('task_type','user','start_time')
    readonly_fields = models.TaskLog._meta.get_all_field_names()
    def has_add_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def total_task(self,obj):
        return obj.tasklogdetail_set.select_related().count()
    def success_task(self,obj):
        return obj.tasklogdetail_set.select_related().filter(result='success').count()
    def failed_task(self,obj):
        return obj.tasklogdetail_set.select_related().filter(result='failed').count()
    def unknown_task(self,obj):
        data = "<a href='#'> %s </a>" % obj.tasklogdetail_set.select_related().filter(result='unknown').count()
        return data
    unknown_task.allow_tags = True

class TaskLogDetailAdmin(admin.ModelAdmin):
    list_display = ('child_of_task','bind_host','result','date')
    list_filter = ('child_of_task','result','date')
    def suit_row_attributes(self,obj,request):
        css_class = {
            'success': 'success',
            'unknown': 'warning',
            'failed': 'error',
        }.get(obj.result)
        if css_class:
            return {'class':css_class,'data':obj.result}
    def has_add_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    readonly_fields = models.TaskLogDetail._meta.get_all_field_names()
class TokenAdmin(admin.ModelAdmin):
    list_display = ('user','host','token','date','expire')
    def has_add_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    #不同权限的可以编辑不同的内容，可以通过get_readonly_fileds()来添加字段只读权限。
    readonly_fields = models.Token._meta.get_all_field_names()

admin.site.register(models.Hosts,HostAdmin)
admin.site.register(models.BindHosts,BindHostAdmin)
admin.site.register(models.HostGroups,HostGroupAdmin)
admin.site.register(models.HostUsers,HostUserAdmin)
admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models. AuditLog,AuditLogAdmin)
admin.site.register(models.TaskLog,TaskLogAdmin)
admin.site.register(models.TaskLogDetail,TaskLogDetailAdmin)
admin.site.register(models.Token,TokenAdmin)
admin.site.register(models.IDC)
admin.site.register(models.Department)


