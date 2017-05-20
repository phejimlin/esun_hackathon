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





function search_submit(){
    var search_query = document.getElementById("input_v").value;
    console.log(search_query);
    console.log(currentURL);
    $.ajax({
        type:'GET',
        url: currentURL.origin + '/api/profile?other_ssn=' +search_query,
        success:function(response){
            result = response;
            console.log(response);
            alert(result);
        },
        error:function(error){
            console.log(error);
        }
    });
}