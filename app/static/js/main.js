var currentURL = window.location;
function init_person(){
    var queryName = getParameterByName('name', currentURL.href);
    var url = currentURL.origin + '/api/profile';

    // For query other people!
    if (queryName) {
        url += '?name='+queryName
    }

	$.ajax({
        type:'GET',
        url: url,
        success:function(response){
            result = response;
            console.log(result);
            var name = result['name'];
            var email = result['email'];
            var eth_address = result['eth_address'];
            var emo = result['emo'];
            var peo = result['peo'];
            var sn = result['sn'];
            var risk = result['risk'];
            var idt = result['idt'];
            var sad = result['emo_freq_sad'];
            var haha = result['emo_freq_haha'];
            var wow = result['emo_freq_wow'];
            var angry = result['emo_freq_angry'];
            var love = result['emo_freq_love'];
            var credit_score = result['credit_score'];
            var about_me = result['about_me'];

            $('#usr_name').append(name);
            $('#usr_email').append(email);

            if (credit_score <= 950 && credit_score > 850){
                $('#credit_score').append(credit_score + '(高)');
            }
            else if (credit_score <= 850 && credit_score > 650){
                $('#credit_score').append(credit_score + '(中高)');
            }
            else if (credit_score <= 650 && credit_score > 550){
                $('#credit_score').append(credit_score + '(中)');
            }
            else if (credit_score <= 550 && credit_score > 450){
                $('#credit_score').append(credit_score + '(低)');
            }
            else{
                $('#credit_score').append(credit_score + '(低)');
            }


            var ctx = $("#myChart");
            var data = {
                labels: ["情緒互動", "人脈連結", "社群評論", "身份特質", "風險程度"],
                datasets: [
                    {
                        label: "iCredible Component",
                        backgroundColor: "rgba(2, 89, 78,0.4)",
                        borderColor: "rgba(2, 89, 78,1)",
                        pointBackgroundColor: "rgba(179,181,198,1)",
                        pointBorderColor: "#fff",
                        pointHoverBackgroundColor: "#fff",
                        pointHoverBorderColor: "rgba(179,181,198,1)",
                        data: [emo, peo, sn, risk, idt]
                    },
                ]
            };

            var options = {
                legend: {
                    display: true,
                    labels: {
                        fontSize: 18
                    }
                },
                maintainAspectRatio: true
            }

            var myRadarChart = new Chart(ctx, {
                type: 'radar',
                data: data,
                options: options
            });


            var ctx_emo = $("#myEmotion");
            var data_emo = {
                labels: ["Sad", "Haha", "Wow", "Angry", "Love"],
                datasets: [
                    {
                        label: "Five Emotion",
                        backgroundColor: "rgba(246, 166, 35, 0.4)",
                        borderColor: "rgba(246, 166, 35, 1)",
                        pointBackgroundColor: "rgba(179,181,198,1)",
                        pointBorderColor: "#fff",
                        pointHoverBackgroundColor: "#fff",
                        pointHoverBorderColor: "rgba(179,181,198,1)",
                        data: [sad, haha, wow, angry, love]
                    },
                ]
            };

            var options_emo = {
                legend: {
                    display: true,
                    labels: {
                        fontSize: 18
                    }
                },
                maintainAspectRatio: true
            }

            var myRadarEmotion = new Chart(ctx_emo, {
                type: 'radar',
                data: data_emo,
                options: options_emo
            });

            setTimeout("init_comments()", 6000);
        },
        error:function(error){
            console.log(error);
        }
    });
    

}
function init_comments(){

    $.ajax({
        type:'GET',
        url: currentURL.origin + '/api/feedback/received_from_all',
        success:function(response){
            result1 = response;
            for (var element in result1){
                var score = element[0];
                var item = element[1];
                var name = element[2];
                var msg = element[3];

                $('#table1').append('<tr><td>'+score+'</td><td>'+item+'</td><td>'+name+'</td><td>'+msg+'</td></tr>');
            }

        },
        error:function(error){
            console.log(error);
        }
    });


    $.ajax({
        type:'GET',
        url: currentURL.origin + '/api/feedback/received_from_buyer',
        success:function(response){
            result2 = response;
            for (var element in result1){
                var score = element[0];
                var item = element[1];
                var name = element[2];
                var msg = element[3];

                $('#table2').append('<tr><td>'+score+'</td><td>'+item+'</td><td>'+name+'</td><td>'+msg+'</td></tr>');
            }

        },
        error:function(error){
            console.log(error);
        }
    });

    $.ajax({
        type:'GET',
        url: currentURL.origin + '/api/feedback/received_from_seller',
        success:function(response){
            result3 = response;
            for (var element in result1){
                var score = element[0];
                var item = element[1];
                var name = element[2];
                var msg = element[3];

                $('#table3').append('<tr><td>'+score+'</td><td>'+item+'</td><td>'+name+'</td><td>'+msg+'</td></tr>');
            }

        },
        error:function(error){
            console.log(error);
        }
    });

    $.ajax({
        type:'GET',
        url: currentURL.origin + '/api/feedback/sent',
        success:function(response){
            result4 = response;
            for (var element in result4){
                var score = element[0];
                var item = element[1];
                var name = element[2];
                var msg = element[3];

                $('#table4').append('<tr><td>'+score+'</td><td>'+item+'</td><td>'+name+'</td><td>'+msg+'</td></tr>');
            }

        },
        error:function(error){
            console.log(error);
        }
    });
}

function search_submit(){
    var search_query = document.getElementById("input_v").value;
    var redirectUrl = currentURL.origin + '/index?name=' +search_query
    var url = currentURL.origin + '/api/profile?name=' +search_query
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