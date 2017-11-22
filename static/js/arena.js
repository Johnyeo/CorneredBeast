/**
 * Created by zhangyao on 2017/10/24.
 */
//处理csrf
jQuery(document).ajaxSend(function (event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
//正文
$(document).ready(function () {
    // 横坐标，纵坐标，方向
    var currentPosition = [2,9,1]
    var destination = [5,1]

    //从服务器获取
    var beastList = [
        // {
        //     "name":["名字","dog"],
        //     "health":["健康","10"],
        //     "fightness":["战斗",'10'],
        // },
        [
            ["名字","cat"],
            ["健康","10"],
            ["战斗",'10'],
        ],
        [
            ["名字","dog"],
            ["健康","10"],
            ["战斗",'10'],
        ],
    ];

    //初始化执行
    window.onload = function () {
        //生成网格
        generateGrid();
        generateBeastCube('cat');
        generateBeastCube('dog');
        initBeastSkill();
        echart();
    };

    function echart() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echarts'));

        // 指定图表的配置项和数据
        var option = {
            title: {
                text: 'ECharts 入门示例'
            },
            tooltip: {},
            legend: {
                data:['销量']
            },
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

    }

    //初始化运行，生成网格
    function generateGrid() {
        //网格
        var grid_row = [0,1,2,3,4,5,6,7,8,9,]
        var grid_column =[0,1,2,3,4,5,6,7,8,9,]
        //循环生成网格
        $.each(grid_column, function () {
            var id_c = this
            $("#grid").append("<div id='row_"+id_c+"' class='grid_row'>")
            var current_row = "#row_" + id_c
                $.each(grid_row, function(){
                var position_id = "block_"+ id_c + this;
                $(current_row).append('<div class="block" id='+position_id+ '></div>')
                 });
        });
    }

    //生成动物
    function generateBeastCube(beast_name) {
        var beast_x = [0,1,2,3];
        var beast_y = [0,1,2,3];
        //循环生成网格
        $("#beast").append("<div id='"+ beast_name +"'>");
        $("#"+beast_name).append("<div style='margin-bottom: 10px'>"+ beast_name +"</div>")
        $.each(beast_y, function () {
            var id_c = this
            $("#"+beast_name).append("<div id='row_"+beast_name+id_c+"' class='beast_row'>");
            var current_row = "#row_" + beast_name + id_c;
                $.each(beast_x, function(){
                var position_id = "block_"+beast_name+ id_c + this;
                $(current_row).append('<div class="block" id='+position_id+ '></div>');
                 });
        });
    }

    //输入目标横纵坐标和方向
    function moveto (current, desti) {
        var x0 = current[0];
        var y0 = current[1];
        var r0 = current[2];
        var x1 = desti[0];
        var y1 = desti[1];
        var r1 //没用
        var x_ok = false;
        var y_ok = false;

        step(x0,y0,r0)

        var timer = setInterval(function () {
            if ((!x_ok) || (!y_ok)){
            var xy;
            if (y_ok){
                xy = 0;
                console.log("xy = 0;")
            } else if (x_ok){
                xy = 1;
                console.log("xy = 1;")
            } else {
                xy = Math.floor(Math.random()*2);
                console.log("xy = random;")
            }

            //比较判断下一个点,随机比较x或者y

            if (xy === 0){
                if((x1-x0)>0){
                    x0 = x0 + 1;
                    step(x0, y0, 1)
                    console.log("x0 = x0 + 1;")
                }
                else if((x1-x0)<0){
                    x0 = x0 - 1;
                    step(x0, y0, 3)
                    console.log("x0 = x0 - 1;")
                }
                else {
                    x_ok = true;
                    console.log("x0_ok")
                }
            }
            else if (xy === 1) {
                if ((y1-y0)>0){
                    y0 = y0 + 1;
                    step(x0, y0, 2)
                    console.log("y0 = y0 + 1;")
                } else if ((y1-y0)<0){
                    y0 = y0 - 1;
                    step(x0, y0, 0)
                    console.log("y0 = y0 - 1;")
                } else {
                    y_ok = true;
                    console.log("y_ok;")
                }
            }
        }
            else {
            clearInterval(timer)
            }
        },1000)
    }

    // 在 x，y的位置显示
    function step(x,y,r) {
        // $("#grid>").remove()
        // generateGrid()
        var block_id = "#block_"+y+x;
        
        switch(r)
        {
        case 0:
            $(block_id).removeClass()
            $(block_id).attr("class","beast-head-up");
            break;
        case 1:
            $(block_id).attr("class","beast-head-right");
            break;
        case 2:
            $(block_id).attr("class","beast-head-down");
            break;
        case 3:
            $(block_id).attr("class","beast-head-left");
            break;
        default:
            $(block_id).attr("class","block");
            break;
        }
    }

    //显示动物数据
    function initBeastSkill() {
        $.each(beastList, function () {
            var name = this[0][1];
            $("#"+ name).append('<div class="skill">');
            $.each(this, function () {
                console.log(this)
                $("#"+ name + " .skill").append('<div><span>'+ this[0] + '：</span><span class="name">'+ this[1] +'</span></div>');
            })
        })
    }

    function updateBeast(index, seed) {
        switch (seed){
            // block_quickness
            case 0:
                beastList[index].push(['敏捷','+1'])
                console.log("quickness");
                break;
            // block_strength
            case 1:
                beastList[index].push(['强壮','+1']);
                console.log("strength");
                break;
            // block_health
            case 2:
                beastList[index].push(['血量','+1']);
                console.log("health");
                break;
            // block_defence
            case 3:
                beastList[index].push(['防守','+1']);
                console.log("defence");
                break;
            // none
            default:

            };
        $("#beast .skill").remove();
        initBeastSkill();



    }

    // 按钮触发的
    //开始移动
    $("#move_to").click(function () {
        moveto(currentPosition,destination)
    });

    //初始化一个点
    $("#set_positon").click(function () {
        var x = currentPosition[0]
        var y = currentPosition[1]
        var r = currentPosition[2]
        //刷新地图
        $("#grid>").remove()
        generateGrid()
        var block_id = "#block_"+y+x;
        switch(r)
        {
        case 0:
            $(block_id).removeClass()
            $(block_id).attr("class","beast-head-up");
            alert(block_id)
            break;
        case 1:
            $(block_id).attr("class","beast-head-right");
            break;
        case 2:
            $(block_id).attr("class","beast-head-down");
            break;
        case 3:
            $(block_id).attr("class","beast-head-left");
            break;
        default:
            $(block_id).attr("class","block");
            break;
        }

    });

    //点击发送按钮，放置野兽
    $("#send").click(function () {
        //输入的值
        var input_val;
        //要染色的block的id
        var colored_pos
        //获取输入值
        input_val = $("#locate").val()
        colored_pos = "#block_"+ input_val
        $(colored_pos).attr("class","beast-head-up")
    });

    //点击网格小方块执行（grid里动态生成的.block执行）
    $("#grid").on("click", ".block", function () {
        //默认block_id是0
        var block_id = "0";
        //点击小的block，改变class，变色
        $(this).attr("class", function(i,origValue){
            return "block-active";
        });
        //获取当前的点击的block的id
        $(this).attr("id", function(i,origValue){
            block_id = origValue
        });
        //返回block_id
    });

    //点击网格小方块，抽技能点
    $("#beast").on("click",".block",function () {
        //默认block_id是0
        var block_id = "0";
        var beast_index = 1;
        var seed = Math.floor(Math.random()*4);
        console.log(seed);
        switch (seed){
            case 0:
                //点击小的block，改变class，变色
                $(this).attr("class", function(i,origValue){
                    return "block_quickness";
                });
                // 增加属性
                updateBeast(beast_index, seed);
                //获取当前的点击的block的id
                $(this).attr("id", function(i,origValue){
                    block_id = origValue
                });
                //返回block_id
                break;
            case 1:
                //点击小的block，改变class，变色
                $(this).attr("class", function(i,origValue){
                    return "block_strength";
                });
                // 增加属性
                updateBeast(beast_index, seed);
                //获取当前的点击的block的id
                $(this).attr("id", function(i,origValue){
                    block_id = origValue
                });
                //返回block_id
                break;
            case 2:
                //点击小的block，改变class，变色
                $(this).attr("class", function(i,origValue){
                    return "block_health";
                });
                // 增加属性
                updateBeast(beast_index, seed);
                //获取当前的点击的block的id
                $(this).attr("id", function(i,origValue){
                    block_id = origValue
                });
                //返回block_id
                break;
            case 3:
                //点击小的block，改变class，变色
                $(this).attr("class", function(i,origValue){
                    return "block_defence";
                });
                // 增加属性
                updateBeast(beast_index, seed);
                //获取当前的点击的block的id
                $(this).attr("id", function(i,origValue){
                    block_id = origValue
                });
                //返回block_id
                break;
            default:
                //点击小的block，改变class，变色
                $(this).attr("class", function(i,origValue){
                    return "block";
                });
                //获取当前的点击的block的id
                $(this).attr("id", function(i,origValue){
                    block_id = origValue
                });
                //返回block_id
            };

    });

})

