$(function () {
    var type_icon_is_down = true;
    $("#all_type").click(function () {

        type_icon_is_down = type_icon_toggle(type_icon_toggle);
        // toggle 切换标签元素的显示与隐藏状态
        $("#type_containor").toggle();
    });
    $("#type_containor").click(function () {
        $(this).toggle();
        type_icon_is_down = type_icon_toggle(type_icon_toggle);
    });

//    排序按钮
    $("#all_sorted").click(function () {
        $("#sort_containor").toggle();
    });
    $("#sort_containor").click(function () {
        $(this).toggle();
    })

//    跟加号按钮添加点击事件
    $(".addShopping").click(function () {
        var g_id = $(this).attr("g_id");
        var $current_btn = $(this);
        $.ajax({
            url:"/axf/api/v1/cart",
            data:{
                g_id: g_id,
                operte_type: "add"
            },
            method:"post",
            success:function (res) {
                console.log(res);
                if (res.code == 1){
                //    我要更新span标签上的数字
                    $current_btn.prev().html(res.data);
                }else if(res.code == 3){
                //    处理没登录的情况
                    window.open(url=res.data, target="_self")
                }else {
                    alert(res.msg)
                }
            }
        })
    })
});
//跟减号按钮加点击事件
    $(".subShopping").click(function () {
        var g_id = $(this).attr("g_id");
        var $current_btn = $(this);
        var span_str = $current_btn.next().text();
        if (parseInt(span_str) == 0){
            return ;
        }
        $.ajax({
            url:"/axf/api/v1/cart",
            data:{
                g_id: g_id,
                operate_type: "sub"
            },
        })
    })
function type_icon_toggle(type_icon_is_down) {
    if (type_icon_is_down) {
        $("#type_icon").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        type_icon_is_down = false;
    } else {
        $("#type_icon").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        type_icon_is_down = true;
    }
    return type_icon_is_down;
}

