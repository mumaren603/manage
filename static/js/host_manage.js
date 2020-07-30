
    $(function(){
        //添加操作
        $('#add_btn').click(function () {
            $('.shadow,.add_div').removeClass('hide')
        })

        //添加界面取消按钮
        $('#add_cal_btn').click(function () {
            $('.shadow,.add_div').addClass('hide')
        })

        //编辑界面取消按钮
        $('#edit_cal_btn').click(function () {
            $('.shadow,.edit_div').addClass('hide')
        })

        //添加保存功能
        $('#add_save_btn').click(function () {
            $.ajax({
                url:'/host_add',
                method:'POST',
                data:$('#add_form').serialize(),
                dataType:'JSON',
                success:function(obj){
                    if(obj.code == 0){
                        location.reload()
                    }else{
                        $('#add_error_msg').text(obj.err_msg)
                    }

                }
            })
        })

        //编辑
        $('.edit_btn').click(function () {
            $('.shadow,.edit_div').removeClass('hide')

            //当前主机id获取
            var host_id = $(this).parent().parent().attr('hid')

            //获取基本信息
            var host_name = $(this).parent().parent().find('td[name="host_name"]'). text()
            var host_systemVersion = $(this).parent().parent().find('td[name="host_systemVersion"]'). text()
            var host_username = $(this).parent().parent().find('td[name="host_username"]'). text()
            var host_password = $(this).parent().parent().find('td[name="host_password"]'). text()
            var host_mainboardNo = $(this).parent().parent().find('td[name="host_mainboardNo"]'). text()
            var host_mainboardmodel = $(this).parent().parent().find('td[name="host_mainboardmodel"]'). text()
            var host_CPUlogiccores = $(this).parent().parent().find('td[name="host_CPUlogiccores"]'). text()
            var host_CPUphysicalcores = $(this).parent().parent().find('td[name="host_CPUphysicalcores"]'). text()
            var host_manufacturer = $(this).parent().parent().find('td[name="host_manufacturer"]'). text()
            var host_deptname = $(this).parent().parent().attr('bid')
            //获取网卡信息
            var host_Intranetname = $(this).parent().parent().find('td[name="host_Intranetname"]'). text()
            var host_Intranetmac = $(this).parent().parent().find('td[name="host_Intranetmac"]'). text()
            var host_IntranetIp = $(this).parent().parent().find('td[name="host_IntranetIp"]'). text()
            var host_IntranetNetMask = $(this).parent().parent().find('td[name="host_IntranetNetMask"]'). text()
            var host_IntranetGateWay = $(this).parent().parent().find('td[name="host_IntranetGateWay"]'). text()
            var host_IntranetDNS = $(this).parent().parent().find('td[name="host_IntranetDNS"]'). text()
            var host_Extranetname = $(this).parent().parent().find('td[name="host_Extranetname"]'). text()
            var host_Extranetmac = $(this).parent().parent().find('td[name="host_Extranetmac"]'). text()
            var host_ExtranetIp = $(this).parent().parent().find('td[name="host_ExtranetIp"]'). text()
            var host_ExtranetNetMask = $(this).parent().parent().find('td[name="host_ExtranetNetMask"]'). text()
            var host_ExtranetGateWay = $(this).parent().parent().find('td[name="host_ExtranetGateWay"]'). text()
            var host_ExtranetDNS = $(this).parent().parent().find('td[name="host_ExtranetDNS"]'). text()
            //获取硬件信息
            var host_os = $(this).parent().parent().find('td[name="host_os"]'). text()
            var host_price = $(this).parent().parent().find('td[name="host_price"]'). text()
            var host_cpu = $(this).parent().parent().find('td[name="host_cpu"]'). text()
            var host_memory = $(this).parent().parent().find('td[name="host_memory"]'). text()
            var host_power = $(this).parent().parent().find('td[name="host_power"]'). text()
            var host_disk = $(this).parent().parent().find('td[name="host_disk"]'). text()

            //编辑页面id值回填 用于发给后端数据更新是作为查询条件
            $('#edit_form').find('input[name="host_id"]').val(host_id)

            //基本信息值回填
            $('#edit_form').find('input[name="host_name"]').val(host_name)
            $('#edit_form').find('input[name="host_systemVersion"]').val(host_systemVersion)
            $('#edit_form').find('input[name="host_username"]').val(host_username)
            $('#edit_form').find('input[name="host_password"]').val(host_password)
            $('#edit_form').find('input[name="host_mainboardNo"]').val(host_mainboardNo)
            $('#edit_form').find('input[name="host_mainboardmodel"]').val(host_mainboardmodel)
            $('#edit_form').find('input[name="host_CPUlogiccores"]').val(host_CPUlogiccores)
            $('#edit_form').find('input[name="host_CPUphysicalcores"]').val(host_CPUphysicalcores)
            $('#edit_form').find('input[name="host_manufacturer"]').val(host_manufacturer)
            $('#edit_form').find('select').val(host_deptname)
            //网卡信息回填
            $('#edit_form').find('input[name="host_Intranetname"]').val(host_Intranetname)
            $('#edit_form').find('input[name="host_Intranetmac"]').val(host_Intranetmac)
            $('#edit_form').find('input[name="host_IntranetIp"]').val(host_IntranetIp)
            $('#edit_form').find('input[name="host_IntranetNetMask"]').val(host_IntranetNetMask)
            $('#edit_form').find('input[name="host_IntranetGateWay"]').val(host_IntranetGateWay)
            $('#edit_form').find('input[name="host_IntranetDNS"]').val(host_IntranetDNS)
            $('#edit_form').find('input[name="host_Extranetname"]').val(host_Extranetname)
            $('#edit_form').find('input[name="host_Extranetmac"]').val(host_Extranetmac)
            $('#edit_form').find('input[name="host_ExtranetIp"]').val(host_ExtranetIp)
            $('#edit_form').find('input[name="host_ExtranetNetMask"]').val(host_ExtranetNetMask)
            $('#edit_form').find('input[name="host_ExtranetGateWay"]').val(host_ExtranetGateWay)
            $('#edit_form').find('input[name="host_ExtranetDNS"]').val(host_ExtranetDNS)
            $('#edit_form').find('input[name="host_os"]').val(host_os)
            $('#edit_form').find('input[name="host_price"]').val(host_price)
            $('#edit_form').find('input[name="host_cpu"]').val(host_cpu)
            $('#edit_form').find('input[name="host_memory"]').val(host_memory)
            $('#edit_form').find('input[name="host_power"]').val(host_power)
            $('#edit_form').find('input[name="host_disk"]').val(host_disk)

            $('#edit_save_btn').click(function(){
                $.ajax({
                    url:'/host_edit',
                    type:'POST',
                    data:$('#edit_form').serialize(),
                    dataType: 'JSON',
                    success:function (obj) {
                        if(obj.code==0){
                            console.log(obj.res_msg)
                            location.reload()
                        }else{
                            console.log(obj.res_msg)
                            $('#edit_error_msg').text(obj.err_msg)
                        }
                    }
                })
            })

        })

    })
