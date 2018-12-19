//前后端分离下，经常出现跨域(CORS)问题，这个问题是浏览器的原因造成的，跟后台没有关系。
//一般在当前页面中，请求了和当前域名及端口不一致的url，就会出现跨域；
// 页面：http://localhost:63342 接口：http://localhost:8000
// 浏览器默认情况下阻止跨域：主要是为了保护网站的安全性的一种同源策略，在不确定安全性的前提下，不允许访问和网站本身端口域名不相同的地址的。

// 跨域是浏览器向后台接口发送请求，并且后台也响应了这个请求，但是浏览器的同源策略将这个跨域的响应拦截了。

function loadData(page) {
    // 该函数是根据page的值，加载当前页数据的函数；
    // page: 表示当前页的页码
    list_url = 'http://127.0.0.1:8000/students/?page=' + page + '&size=3';
    $.get(list_url, function(data){
        // 解析后台接口返回的json数据
        // 因为loadData(page)是循环调用的，所以在每次append()之前，先将上一次的数据清空，然后再append()新的数据。
        $('tbody').empty();
        for (var index in data.results){
            var student = data.results[index];
            tr = $('<tr>');
            // 向<tr>标签中添加三个<td>，分别是姓名、ID、年龄
            tr.append($('<td>').text(student.name), $('<td>').text(student.id), $('<td>').text(student.age));
            // 继续向<tr>标签中添加编辑图标和删除图标
            tr.append($('<td>').append($('<span>').attr({
                'class': 'glyphicon glyphicon-edit',
                'data-toggle': 'modal',
                'data-target': '#editModal'
            })));
            tr.append($('<td>').append($('<span>').attr({'class': 'glyphicon glyphicon-remove'})));
            $('tbody').append(tr);
        }
        // 开始设置分页
        $('.pagination').empty();
        if (data.has_previous){
            // 有上一页
            $('.pagination').append($('<li>').append($('<a>').attr({'aria-label': 'Previous', 'href': 'javascript:loadData(' + data.previous_url + ');'}).text('<<')));
        }
        // [2 3 4 5 6]
        for (var index in data.page_nums){
            var page_number = data.page_nums[index];
            var li = $('<li>');
            if (data.current_page == page_number){
                //如果当前请求的页码的值current_page和遍历出来的page_number的值相等，将这个页码标记为选中状态。
                li.attr('class', 'active');
            }
            // 向这个li内部添加一个a标签
            li.append($('<a>').attr({'href': 'javascript:loadData(' + page_number + ');'}).text(page_number));
            // 再将这个li添加到ul标签中；
            $('.pagination').append(li);
        }
        // 下一页
        if (data.has_next){
            $('.pagination').append($('<li>').append($('<a>').attr({'aria-label': 'Next', 'href': 'javascript:loadData(' + data.next_url + ');'}).text('>>')));
        }
    });
}

loadData(1);

// 检查学号是否已经存在
$('#sid').blur(function () {
    //在数据没有合法之前，"提交按钮" 不能点击；
    $('#add').attr('disabled', true);
    $.ajax({
        url: 'http://localhost:8000/inspect/',
        type: 'POST',
        data: {
            'sid': $('#sid').val()
        },
        xhrFields: {
            withCredentials: true
        },
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        },
        success: function (data, status) {
            $('#sid').next().text(data.message);
        }
    });
});

// 发送ajax请求，在页面刷新的时候，就获取csrftoken的值
$(function () {
    $.ajax({
        url: 'http://localhost:8000/token/',
        // 默认情况下，跨域请求的请求头是不允许携带Cookie的，另外一方面，跨域请求的响应头中默认只包含content-type，后台的响应中只返回这一个字段。
        xhrFields: {
            withCredentials: true,
        }
    });
});
