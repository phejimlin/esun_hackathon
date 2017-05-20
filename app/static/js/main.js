var currentURL = window.location;
function init_person(){
	$.ajax({
        type:'GET',
        url: 'http://168.63.204.214/api/profile',
        success:function(response){
            result = response;
            alert(result);
        },
        error:function(error){
            console.log(error);
        }
    });
}