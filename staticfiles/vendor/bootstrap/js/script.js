


// $( document ).ready(function() {
//     var arr = ['bg_1.jpg','bg_2.jpg','bg_3.jpg'];
    
//     var i = 0;
//     setInterval(function(){
//         if(i == arr.length - 1){
//             i = 0;
//         }else{
//             i++;
//         }
//         var img = 'url(../img/'+arr[i]+')';
//         $(".full-bg").css('background-image',img); 
     
//     }, 4000)

// });


$( document ).ready(function() {
    // var arr = ['bg_1.jpg','bg_2.jpg','bg_3.jpg'];
    var arr = ['bg.png','lg.jpg'];
    
    var i = 0;
    setInterval(function(){
        if(i == arr.length - 1){
            i = 0;
        }else{
            i++;
        }
        var img = 'url(../img/'+arr[i]+')';
        $(".full-bg").css('background-image',img); 
     
    }, 4000)

});



