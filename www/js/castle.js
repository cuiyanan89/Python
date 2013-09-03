function load(){
    var ad_btn = document.getElementById("ad_btn");
    var address = document.getElementById("address");
    var time = document.getElementById('time');
    var goods = document.getElementsByName("goods");
    var buy = document.getElementById("menu");
    var no = document.getElementById('no');
    var yes = document.getElementById('yes');
    var textarea = document.getElementById("textarea");
    var good_list = {'哆啦A梦1':10,'哆啦A梦2':9,'哆啦A梦3':8,'哆啦A梦4':7,'哆啦A梦5':6,'哆啦A梦6':5}
    var buy_list = new Array();
    for (var n = 0 ; n < goods.length ; n++ ){
        goods[n].onclick=function(){
            if (this.checked){
                buy_list.push(this.value);
            }else{
                for (n in buy_list){
                    if (buy_list[n]==this.value){
                        buy_list.splice(n,1);
                    }
                }
            }
            buy.innerHTML = '';
            for (n in buy_list){
                buy.innerHTML += buy_list[n] + ":&nbsp;" + good_list[buy_list[n]] + "元<br/>";
            }
        }
    }
    ad_btn.onclick=function(){
        ad_new = prompt("收货地址：","沁园公寓");
        if (ad_new){
            address.innerHTML = ad_new;
        }
    }
    no.onclick = function(){
        buy_list.splice(0,buy_list.length);
        buy.innerHTML = '';
        for (n in goods){
            goods[n].checked = false;
        }
    }
    yes.onclick = function(){
        var name = document.getElementById('name');
        var phone = document.getElementById('phone');
        if (name.value && phone.value){
            var box = '';
            var price = 0;
            for (n in buy_list){
                box += buy_list[n] + ": " + good_list[buy_list[n]] + "元 ";
                price += good_list[buy_list[n]];
            }
            var text_textarea = '';
            if (textarea.value != '' ){
                text_textarea ="备注信息:" + textarea.value +'\n';
            }
            if (buy_list.length != 0){
            alert(name.value + ",您选购的商品为:\n" + box+"\n合计:"+price+"元\n" + text_textarea + "商品将于"+time.options[time.selectedIndex].text+'送至'+address.innerHTML+"请注意查收，谢谢惠顾。");
            }else{
                alert("您没有选购任何商品");
            }
        }else{
            alert('请填写姓名和联系方式');
        }
    }
}
window.onload = load;
