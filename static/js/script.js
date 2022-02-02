$(document).ready(function(){

    if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {

        $.ajax({
            type: 'POST',
            url: "/calculadora",
            data: 'reload',
            success: function(response){
                $('#tela').val(response);
            },
            error: function(error){
                $('#tela').val(error);
            }
        })    

            
       
    }
        


    
    $("button").click(function() {

        var btn_clicked =  $(this).prop('value');


        $.ajax({
            type: 'POST',
            url: "/calculadora",
            data: btn_clicked,
            success: function(response){
                $('#tela').val(response);
            },
            error: function(error){
                $('#tela').val(error);
            }
        })    

        
        
    });



});






