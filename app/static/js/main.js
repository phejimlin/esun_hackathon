var currentURL = window.location;
function init_person(){
	$.ajax({
        type:'GET',
        url: currentURL.origin + '/api/profile',
        success:function(response){
            result = response;
            console.log(result);
            var name = result['name'];
            var email = result['email']

            $('#usr_name').append(name);
            $('#usr_email').append(email);

        },
        error:function(error){
            console.log(error);
        }
    });
}