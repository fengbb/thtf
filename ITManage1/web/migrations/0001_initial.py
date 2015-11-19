# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('action_type', models.IntegerField(default=0, choices=[(0, 'CMD'), (1, 'Login'), (2, 'Logout'), (3, 'GetFile'), (4, 'SendFile'), (5, 'exception')])),
                ('cmd', models.TextField()),
                ('memo', models.CharField(max_length=128, blank=True, null=True)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '审计日志',
                'verbose_name_plural': '审计日志',
            },
        ),
        migrations.CreateModel(
            name='BindHosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '主机与远程用户绑定',
                'verbose_name_plural': '主机与远程用户绑定',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='HostGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('memo', models.CharField(max_length=128, blank=True, null=True)),
            ],
            options={
                'verbose_name': '主机组',
                'verbose_name_plural': '主机组',
            },
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('hostname', models.CharField(max_length=64, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('system_type', models.CharField(max_length=32, default='linux', choices=[('windows', 'Windows'), ('linux', 'Linux/Unix')])),
                ('port', models.IntegerField(default=22)),
                ('enabled', models.BooleanField(default=True, help_text='主机若不想被用户访问可以去掉此选项')),
                ('memo', models.CharField(max_length=128, blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='HostUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('auth_method', models.CharField(max_length=16, help_text='如果选择SSH/KEY，请确保你的私钥文件已在settings.py中指定', choices=[('ssh-password', 'SSH/Password'), ('ssh-key', 'SSH/KEY')])),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64, blank=True, help_text='如果auth_method选择的是SSH/KEY,那此处不需要填写..', null=True)),
                ('memo', models.CharField(max_length=128, blank=True, null=True)),
            ],
            options={
                'verbose_name': '远程用户',
                'verbose_name_plural': '远程用户',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
        ),
        migrations.CreateModel(
            name='SessionTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('task_type', models.CharField(max_length=50, choices=[('cmd', 'CMD'), ('file_send', '批量发送文件'), ('file_get', '批量下载文件')])),
                ('cmd', models.TextField()),
                ('expire_time', models.IntegerField(default=30)),
                ('task_pid', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=100, blank=True, null=True)),
                ('hosts', models.ManyToManyField(to='web.BindHosts')),
            ],
            options={
                'verbose_name': '批量任务',
                'verbose_name_plural': '批量任务',
            },
        ),
        migrations.CreateModel(
            name='TaskLogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event_log', models.TextField()),
                ('result', models.CharField(max_length=30, default='unknown', choices=[('success', 'Success'), ('failed', 'Failed'), ('unknown', 'Unknown')])),
                ('note', models.CharField(max_length=100, blank=True)),
                ('bind_host', models.ForeignKey(to='web.BindHosts')),
                ('child_of_task', models.ForeignKey(to='web.TaskLog')),
            ],
            options={
                'verbose_name': '批量任务日志',
                'verbose_name_plural': '批量任务日志',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('test', models.CharField(max_length=32)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('token', models.CharField(max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire', models.IntegerField(default=300)),
                ('host', models.ForeignKey(to='web.BindHosts')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_end_time', models.DateTimeField()),
                ('bind_hosts', models.ManyToManyField(verbose_name='授权主机', to='web.BindHosts')),
                ('department', models.ForeignKey(verbose_name='部门', to='web.Department')),
                ('host_group', models.ManyToManyField(verbose_name='授权主机组', to='web.HostGroups')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CrazyEye账户',
                'verbose_name_plural': 'CrazyEye账户',
            },
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(to='web.UserProfile'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='user',
            field=models.ForeignKey(to='web.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='hostusers',
            unique_together=set([('auth_method', 'password', 'username')]),
        ),
        migrations.AddField(
            model_name='hosts',
            name='idc',
            field=models.ForeignKey(to='web.IDC'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host',
            field=models.ForeignKey(to='web.Hosts'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host_group',
            field=models.ManyToManyField(to='web.HostGroups'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host_user',
            field=models.ForeignKey(to='web.HostUsers'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='host',
            field=models.ForeignKey(to='web.BindHosts'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='session',
            field=models.ForeignKey(to='web.SessionTrack'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='user',
            field=models.ForeignKey(to='web.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosts',
            unique_together=set([('host', 'host_user')]),
        ),
    ]
