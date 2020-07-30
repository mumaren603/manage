from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models
import json

# 登录
def login(request):
    error_msg = ''
    if request.method =='GET':
        return render(request,'login.html',{'error_msg':error_msg})
    elif request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserInfo.objects.filter(
            username=user,
            password=pwd
        ).first()
        if obj:
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误'
            return render(request,'login.html',{'error_msg':error_msg})

# 主页-index
def index(request):
    return render(request,'home-index.html')

# 主页-主机管理(包括分页功能)
def host(request):
    if request.method =='GET':
        # 获取所有主机信息
        host_info = models.Host.objects.all()
        # 总条数
        total_data_count = len(host_info)   #hostinfo返回的是QuerySet,每一个对象即一条数据
        # 获取业务线数据 用于页面添加、编辑功能部门下拉框值选择
        b_info = models.Business.objects.all()

        # 分页功能
        # 当前页
        current_page = request.GET.get('page',1)
        current_page = int(current_page)

        # 每页显示数据（固定7行）
        per_page_data = 7

        start_id = (current_page-1)*7   # 用于页面显示主机按序号递增，{{ forloop.counter|add:start_id }}
        # 每页显示行数
        # 第1页  0-6
        # 第2页  7-13
        start_v = (current_page-1)*7
        end_v = current_page*7

        # 根据行数动态展示页面数据
        host_data = host_info[start_v:end_v]

        # 根据表中总的数据条数确定总的页码个数（如：数据库总条数100条，每页显示7条 那么总页码就需要15个）
        total_page_count,y = divmod(total_data_count,per_page_data)
        if y:
            total_page_count += 1

        page_list = []

        if total_page_count < 9:
            start_index=1
            end_index = total_page_count+1
        else:
            if current_page <=6:
                start_index = 1
                end_index = 9+1
            else:
                start_index = current_page-5
                end_index = current_page+5+1
                if(current_page+5) > total_page_count:
                    satrt_index = total_page_count -9 +1
                    end_index = total_page_count+1

        if current_page == 1:
            prev = '<a class="page" href="javascript:void(0)">上一页</a>'
        else:
            prev = '<a class="page" href="/home/host?page=%s">上一页</a>' % (current_page - 1)
        page_list.append(prev)
        # 根据总的页码动态显示到前端

        # page_list = []
        # for i in range(1,total_page_count+1):
        for i in range(start_index,end_index):
            if i == current_page:
                temp_page = '<a class="page active" href="/home/host?page=%s">%s</a>' %(i,i)
            else:
                temp_page = '<a class="page" href="/home/host?page=%s">%s</a>' %(i,i)
            page_list.append(temp_page)

        if current_page == total_page_count:
            next = '<a class="page" href="javascript:void(0)">下一页</a>'
        else:
            next = '<a class="page" href="/home/host?page=%s">下一页</a>' % (current_page + 1)
        page_list.append(next)

        jump = '''
        <input type="text"/><a onclick="jumpTo(this,'/home/host?page=')">跳转</a>
        <script>
            function jumpTo(ths,base){
                val = ths.previousSibling.value;
                if(!val){
                    val = 1       //如果跳转页输入为空，默认跳转到第一页
                }
                location.href = base + val; 
            }
        </script>
        '''
        page_list.append(jump)

        page_str = ''.join(page_list)

        from django.utils.safestring import mark_safe
        page_str = mark_safe(page_str)
        return render(request,'home-host.html',{'host_data':host_data,'b_info':b_info,'page_str':page_str,'start_id':start_id})


# 主机-添加
def host_add(request):
    if request.method =='POST':
        res_msg = {'code': 0, 'err_msg': None,'data':None}
        try:
            #基本信息
            host_name = request.POST.get('host_name')
            host_systemVersion = request.POST.get('host_systemVersion')
            host_username = request.POST.get('host_username')
            host_password = request.POST.get('host_password')
            host_mainboardNo = request.POST.get('host_mainboardNo')
            host_mainboardmodel = request.POST.get('host_mainboardmodel')
            host_CPUlogiccores = request.POST.get('host_CPUlogiccores')
            host_CPUphysicalcores = request.POST.get('host_CPUphysicalcores')
            host_manufacturer = request.POST.get('host_manufacturer')
            host_dept = request.POST.get('host_dept')
            #网卡信息
            host_Intranetname =request.POST.get('host_Intranetname')
            host_Intranetmac = request.POST.get('host_Intranetmac')
            host_IntranetIp = request.POST.get('host_IntranetIp')
            host_IntranetNetMask = request.POST.get('host_IntranetNetMask')
            host_IntranetGateWay = request.POST.get('host_IntranetGateWay')
            host_IntranetDNS = request.POST.get('host_IntranetDNS')
            host_Extranetname = request.POST.get('host_Extranetname')
            host_Extranetmac = request.POST.get('host_Extranetmac')
            host_ExtranetIp = request.POST.get('host_ExtranetIp')
            host_ExtranetNetMask = request.POST.get('host_ExtranetNetMask')
            host_ExtranetGateWay = request.POST.get('host_ExtranetGateWay')
            host_ExtranetDNS = request.POST.get('host_ExtranetDNS')
            #硬件信息
            host_os = request.POST.get('host_os')
            host_price = request.POST.get('host_price')
            host_cpu = request.POST.get('host_cpu')
            host_memory = request.POST.get('host_memory')
            host_disk = request.POST.get('host_disk')
            host_power = request.POST.get('host_power')

            if host_name and host_username and host_password and host_IntranetIp and host_ExtranetNetMask and host_ExtranetIp  and host_ExtranetNetMask and host_ExtranetGateWay and host_ExtranetDNS and host_dept:
                models.Host.objects.create(
                    hostname=host_name,
                    systemVersion=host_systemVersion,
                    username=host_username,
                    password=host_password,
                    mainboardNo=host_mainboardNo,
                    mainboardmodel=host_mainboardmodel,
                    CPUlogiccores=host_CPUlogiccores,
                    CPUphysicalcores=host_CPUphysicalcores,
                    manufacturer=host_manufacturer,
                    dept_id=host_dept,
                    Intranetname=host_Intranetname,
                    Intranetmac=host_Intranetmac,
                    IntranetIp=host_IntranetIp,
                    IntranetNetMask=host_IntranetNetMask,
                    IntranetGateWay=host_IntranetGateWay,
                    IntranetDNS=host_IntranetDNS,
                    Extranetname=host_Extranetname,
                    Extranetmac=host_Extranetmac,
                    ExtranetIp=host_ExtranetIp,
                    ExtranetNetMask=host_ExtranetNetMask,
                    ExtranetGateWay=host_ExtranetGateWay,
                    ExtranetDNS=host_ExtranetDNS,
                    os=host_os,
                    price=host_price,
                    power=host_power,
                    cpu=host_cpu,
                    memory=host_memory,
                    disk=host_disk,
                )
                res_msg['data']='新增数据成功'
            else:
                res_msg['code'] = 1
                res_msg['err_msg'] = '必填项不能为空。'
        except Exception as e:
            res_msg['code'] = 1
            res_msg['err_msg'] = '请求错误'
        return HttpResponse(json.dumps(res_msg))

# 主机-编辑
def host_edit(request):
    res_msg={'code':0,'err_msg':None,'data':None}
    if request.method == 'POST':
        try:
            host_id = request.POST.get('host_id')
            #基本信息
            host_name = request.POST.get('host_name')
            host_systemVersion = request.POST.get('host_systemVersion')
            host_username = request.POST.get('host_username')
            host_password = request.POST.get('host_password')
            host_mainboardNo = request.POST.get('host_mainboardNo')
            host_mainboardmodel = request.POST.get('host_mainboardmodel')
            host_CPUlogiccores = request.POST.get('host_CPUlogiccores')
            host_CPUphysicalcores = request.POST.get('host_CPUphysicalcores')
            host_manufacturer = request.POST.get('host_manufacturer')
            host_dept = request.POST.get('host_dept')
            #网卡信息
            host_Intranetname =request.POST.get('host_Intranetname')
            host_Intranetmac = request.POST.get('host_Intranetmac')
            host_IntranetIp = request.POST.get('host_IntranetIp')
            host_IntranetNetMask = request.POST.get('host_IntranetNetMask')
            host_IntranetGateWay = request.POST.get('host_IntranetGateWay')
            host_IntranetDNS = request.POST.get('host_IntranetDNS')
            host_Extranetname = request.POST.get('host_Extranetname')
            host_Extranetmac = request.POST.get('host_Extranetmac')
            host_ExtranetIp = request.POST.get('host_ExtranetIp')
            host_ExtranetNetMask = request.POST.get('host_ExtranetNetMask')
            host_ExtranetGateWay = request.POST.get('host_ExtranetGateWay')
            host_ExtranetDNS = request.POST.get('host_ExtranetDNS')
            #硬件信息
            host_os = request.POST.get('host_os')
            host_price = request.POST.get('host_price')
            host_cpu = request.POST.get('host_cpu')
            host_memory = request.POST.get('host_memory')
            host_disk = request.POST.get('host_disk')
            host_power = request.POST.get('host_power')

            if host_name and host_username and host_password and host_IntranetIp and host_ExtranetNetMask and host_ExtranetIp and host_ExtranetNetMask and host_ExtranetGateWay and host_ExtranetDNS and host_dept:
                models.Host.objects.filter(hid=host_id).update(
                    hostname=host_name,
                    systemVersion=host_systemVersion,
                    username=host_username,
                    password=host_password,
                    mainboardNo=host_mainboardNo,
                    mainboardmodel=host_mainboardmodel,
                    CPUlogiccores=host_CPUlogiccores,
                    CPUphysicalcores=host_CPUphysicalcores,
                    manufacturer=host_manufacturer,
                    dept_id=host_dept,
                    Intranetname=host_Intranetname,
                    Intranetmac=host_Intranetmac,
                    IntranetIp=host_IntranetIp,
                    IntranetNetMask=host_IntranetNetMask,
                    IntranetGateWay=host_IntranetGateWay,
                    IntranetDNS=host_IntranetDNS,
                    Extranetname=host_Extranetname,
                    Extranetmac=host_Extranetmac,
                    ExtranetIp=host_ExtranetIp,
                    ExtranetNetMask=host_ExtranetNetMask,
                    ExtranetGateWay=host_ExtranetGateWay,
                    ExtranetDNS=host_ExtranetDNS,
                    os=host_os,
                    price=host_price,
                    power=host_power,
                    cpu=host_cpu,
                    memory=host_memory,
                    disk=host_disk,
                )
                res_msg['data']='更新数据成功'
            else:
                res_msg['code']=1
                res_msg['err_msg']='必填项不能为空。。'
        except Exception as e:
            print(e)
            res_msg['code'] = 1
            res_msg['err_msg'] = '请求错误。'
    return HttpResponse(json.dumps(res_msg))

# 主机-详情
def host_detail(request,nid):
    print("当前页面id为:",nid)
    host_detail = models.Host.objects.filter(hid = nid).first()
    print(host_detail,type(host_detail))
    return render(request,'home-detail.html',{'host_detail':host_detail})

# 主机-删除
def host_del(request,nid):
    models.Host.objects.filter(hid=nid).delete()
    return redirect('/home/host')


# 主页-IP池
from django.db.models import Q
# def ipPool(request):
#     if request.method == 'GET':
#         dept = models.Business.objects.all()
#         return render(request,'ipPool.html',{'dept':dept})
#     elif request.method == 'POST':
#         res_msg={'code':0,'err_msg':None,'data':None}
#         try:
#             ip_addr = request.POST.get('ip_addr')
#             print('ip_addr',ip_addr)
#             ip_netmask = request.POST.get('ip_netmask')
#             print('ip_netmask', ip_netmask)
#             ip_owner = request.POST.get('ip_owner')
#             print('ip_owner', ip_owner)
#             ip_type = request.POST.get('ip_type')
#             print('ip_type', ip_type)
#             ip_group = request.POST.get('ip_group')
#             print('ip_group', ip_group)
#
#             # 定一个字典用于保存前端发送过来的查询条件，前端发送的条件可能是一个或多个，这就需要把不同条件组合起来。
#             search_dict = {}
#             # 如果有这个值 就写入到字典中去
#             if ip_addr:
#                 search_dict['addr'] = ip_addr
#             if ip_netmask:
#                 search_dict['netmask'] = ip_netmask
#             if ip_owner:
#                 search_dict['owner'] = ip_owner
#             if ip_type:
#                 search_dict['ip_type'] = ip_type
#             if ip_group:
#                 search_dict['relgroup_id'] = ip_group
#             print('查询参数是:',search_dict)
#
#             if search_dict:
#                 # 多条件查询 关键点在这个位置传字典前面一定要加上两个星号.
#                 ip_data = models.ippool.objects.filter(**search_dict)
#                 if ip_data.first():
#                     pass
#                 else:
#                     res_msg['code'] = 1
#                     res_msg['err_msg'] = "查询成功，无结果返回。"
#             else:
#                 res_msg['code'] = 1
#                 res_msg['err_msg'] = '请至少输入一个查询条件。'
#         except Exception as e:
#             res_msg['code'] = 1
#             res_msg['err_msg'] = '请求错误。'
#         return HttpResponse(json.dumps(res_msg))

def ipPool(request):
    if request.method == 'GET':
        dept = models.Business.objects.all()
        return render(request,'ipPool.html',{'dept':dept})
    elif request.method == 'POST':
        try:
            ip_addr = request.POST.get('ip_addr')
            print('ip_addr',ip_addr)
            ip_netmask = request.POST.get('ip_netmask')
            print('ip_netmask', ip_netmask)
            ip_owner = request.POST.get('ip_owner')
            print('ip_owner', ip_owner)
            ip_type = request.POST.get('ip_type')
            print('ip_type', ip_type)
            ip_group = request.POST.get('ip_group')
            print('ip_group', ip_group)

            # 定义一个字典用于保存前端发送过来的查询条件，前端发送的条件可能是一个或多个，这就需要把不同条件组合起来。
            search_dict = {}
            # 如果存在某个查询条件 就写入到字典中去
            if ip_addr:
                search_dict['addr'] = ip_addr
            if ip_netmask:
                search_dict['netmask'] = ip_netmask
            if ip_owner:
                search_dict['owner'] = ip_owner
            if ip_type:
                search_dict['ip_type'] = ip_type
            if ip_group:
                search_dict['relgroup_id'] = ip_group
            print('查询条件是:',search_dict)

            if search_dict:
                # 多条件查询 关键点在这个位置传字典前面一定要加上两个星号.
                ip_data = models.ippool.objects.filter(**search_dict)
                dept = models.Business.objects.all()
            else:
                #考虑 查询不到数据如何在前端显示
                pass
        except Exception as e:
                raise
        return render(request,'ipPool.html',{'ip_data':ip_data,'dept':dept})



# 数据泵操作
def sjbTool(request):
    if request.method == 'GET':
        return render(request,'sjb.html')
    elif request.method == 'POST':
        res_msg={'code':0,'err_msg':None,'msg':None}
        try:
            opertion = request.POST.get('opertion')
            print('opertion', opertion)
            sid = request.POST.get('sid')
            print('sid', sid)
            db_name = request.POST.get('db_name')
            print('db_name',db_name)
            content = request.POST.get('content')
            print('content', content)
            directory = request.POST.get('directory')
            print('directory', directory)
            dumpfile = request.POST.get('dumpfile')
            print('dumpfile', dumpfile)
            logfile = request.POST.get('logfile')
            print('logfile', logfile)

            # 校验必填参数是否有值
            if opertion and sid and db_name and dumpfile and directory:
                # 判断文件名在当前目录下是否存在
                data_dir = 'E:\data'   # 服务器上物理路径
                data_dir = data_dir+directory
                import os
                if True:
                # if os.path.exists(data_dir):
                    # 根据content，logfile值拼接脚本
                    if logfile:
                        cmd_script = opertion + ' ' + db_name + '@' + sid + ' ' + "directory=" + directory + ' ' + "dumpfile=" + dumpfile + '.dmp' + ' ' + "content=" + content + ' ' + "logfile=" + logfile + '.log'
                    else:
                        cmd_script = opertion + ' ' + db_name + '@' + sid + ' ' + "directory=" + directory + ' ' + "dumpfile=" + dumpfile + '.dmp' + ' ' + "content=" + content
                    print("脚本:",cmd_script)

                    # res_msg['msg'] = "参数正确，开始执行%s操作。" % opertion

                    # 测试脚本
                    cmd_script = "ipconfig /all"

                    # 执行cmd命令
                    cmd_obj = os.popen(cmd_script)
                    # 这里要考虑 如何把输出日志回传到前端  还有持续输出日志如何在前端显示？
                    with os.popen(cmd_script) as f:
                        data = f.read()
                        print("data",data)
                    res_msg['msg'] = data

                    # https://www.v2ex.com/t/506024
                    # https://www.cnblogs.com/luoxiaowei/p/6952104.html
                    # output = []
                    # for line in data.splitlines():
                    #     output.append(line)
                    # res_msg['msg'] = output

                else:
                    res_msg['code'] = 1
                    res_msg['err_msg'] = "%s该目录在服务器不存在,请检查目录正确性。" %directory
            else:
                res_msg['code']=1
                res_msg['err_msg']="必填参数必填。"
        except Exception as e:
            res_msg['code'] = 1
            res_msg['err_msg'] = "请求错误。"
            raise
        return HttpResponse(json.dumps(res_msg))










'''初始化数据'''
# 创建用户
from app01 import models
def orm_userinfo(request):
    models.UserInfo.objects.create(
        username='lls',
        password='123456'
    )
    return HttpResponse("用户创建成功")

# 创建业务线
def orm_business(request):
    business_list={'测试':'test','开发':'dev','产品':'prod','数据':'dba'}

    for k,v in business_list.items():
        models.Business.objects.create(
            deptname=k,
            deptcode=v
        )
    return HttpResponse("业务线信息创建成功")

# 创建主机
def orm_host(request):
    for i in range(5):
        models.Host.objects.create(
            hostname='www.xxx'+str(i)+'.com',
            ip='1.1.1.1',
            mac='xxxxxxxx',
            os='lINUX',
            price='11000',
            cpu='Intel',
            memory='金士顿32G',
            disk='西数固态1T',
            power='长城500',
            dept_id='1'
    )
    return HttpResponse("主机信息创建成功")

# 创建IP资源池
def orm_ip(request):
    for i in range(5):
        models.ippool.objects.create(
            addr = '172.0.0.'+str(i),
            netmask='255.255.0.0',
            gateway='172.17.16.1',
            ip_type_id=2,
            relgroup_id=2
    )
    return HttpResponse("IP信息创建成功")



