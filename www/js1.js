            window.onload=init;
            window.onunload = unload;
            function init(){
                var text = document.getElementById("text");
                var msg = document.getElementById("msg");
                text.onblur = validusername;
            }
            function unload(){
                alert("byebye");
            }
            function validusername(){
                var textvalue = text.value;
                msg.innerHTML = (textvalue.length<6)?"name is too short":"ok valid";
            }
