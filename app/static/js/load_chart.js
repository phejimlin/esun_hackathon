$( document ).ready(function() {
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
	            data: [12, 19, 3, 17, 28]
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
});