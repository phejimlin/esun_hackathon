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
            $('#credit_score').append(credit_score);
            $("#usr_store a").attr("href", about_me);



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
            result = response;
            console.log(result);

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