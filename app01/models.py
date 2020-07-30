from django.db import models

# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=32,db_index=True)
    password = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)


# 主机
class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True,null=False)
    systemVersion = models.CharField(max_length=64,null=True)
    mainboardNo = models.CharField(max_length=32,null=True)
    mainboardmodel = models.CharField(max_length=32,null=True)
    manufacturer = models.CharField(max_length=32, null=True)
    CPUlogiccores = models.IntegerField(max_length=3,null=True)
    CPUphysicalcores = models.IntegerField(max_length=3, null=True)

    Intranetname = models.CharField(max_length=32, null=True)
    Intranetmac = models.CharField(max_length=32, null=True)
    IntranetIp = models.GenericIPAddressField(max_length=20,db_index=True,null=False,default='172.0.0.248')
    IntranetNetMask = models.CharField(max_length=20,null=False,default='255.255.255.0')
    IntranetGateWay = models.CharField(max_length=20,null=True)
    IntranetDNS = models.CharField(max_length=20,null=True)
    Extranetname = models.CharField(max_length=32, null=True)
    Extranetmac = models.CharField(max_length=32, null=True)
    ExtranetIp = models.GenericIPAddressField(max_length=20,db_index=True,null=False,default='192.168.1.248')
    ExtranetNetMask = models.CharField(max_length=20,null=False,default='255.255.255.0')
    ExtranetGateWay = models.CharField(max_length=20,null=False,default='192.168.1.1')
    ExtranetDNS = models.CharField(max_length=20,null=False,default='218.3.5.153')
    username = models.CharField(max_length=32,null=False,default='administrator')
    password = models.CharField(max_length=32, null=False,default='123123')
    # os_type_choices=(
    #     (1,'WINDOWS'),
    #     (2,'UNIX'),
    #     (3,'LINUX'),
    #     (4,'NETWARE'),
    # )
    # os_type_id = models.IntegerField(choices=os_type_choices,default=1)
    os = models.CharField(max_length=32,default='WindowsServer2012')
    price = models.CharField(max_length=10,null=True)
    cpu = models.CharField(max_length=32,null=True)
    memory = models.CharField(max_length=32,null=True)
    disk = models.CharField(max_length=32,null=True)
    power = models.CharField(max_length=32,null=True)
    dept = models.ForeignKey('Business',to_field='id',null=False,on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

#业务线
class Business(models.Model):
    # id 自增
    deptname = models.CharField(max_length=32,null=False)
    deptcode = models.CharField(max_length=12)

# ip池
class ippool(models.Model):
    ipid = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=32,null=False,db_index=True)
    addr = models.GenericIPAddressField(max_length=20,null=False,db_index=True)
    netmask =models.CharField(max_length=20,null=True)
    gateway = models.CharField(max_length=20, null=True)
    dns= models.CharField(max_length=20, null=True)
    ip_type = models.CharField(max_length=20,null=True,default='个人IP')
    # 所属组
    relgroup = models.ForeignKey('Business',to_field='id',on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

