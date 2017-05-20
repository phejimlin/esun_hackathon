var currentURL = window.location;
function init_person(){
    var queryName = getParameterByName('other_ssn', currentURL.href)
    var url = currentURL.origin + '/api/profile'

    // For query other people!
    if (queryName) {
        url += '?other_ssn='+queryName
    }

	$.ajax({
        type:'GET',
        url: url,
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





function search_submit(){
    var search_query = document.getElementById("input_v").value;
    var redirectUrl = currentURL.origin + '/index?other_ssn=' +search_query
    var url = currentURL.origin + '/api/profile?other_ssn=' +search_query
    $.ajax({
        type:'GET',
        url: url,
        success:function(response){
            window.location = redirectUrl;
        },
        error:function(error){
            console.log(error);
            if (error.status == 404){
                alert("查無此人，請再次搜尋。")
            }
        }
    });
}

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}