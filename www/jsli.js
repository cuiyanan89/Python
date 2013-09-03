            function f1(){
                var a_array = document.getElementsByTagName('A');
                for (var n = 0 ; n < a_array.length ; n++ ){
                    a_array[n].href="http://www."+a_array[n].text+".com";
                }
            }
            window.onload = f1;
