var currentURL = window.location;
function resettext(id){
  if(id.value == ""){
    id.value = id.defaultValue;   
  }
}

function cleartext (id){ 
  id.value ="";
}

function login(){
  var id_num = $('#id_num').val();
  var pwd = $('#pwd').val(); 
  
  $.ajax({
    url: '/login',
    data:JSON.stringify({
      "ssn": id_num,
      "password": pwd
    }),
    type:'POST',
    contentType:"application/json",
    datatype:'application/json',
    success:function(response){
      console.log("Just login")

      var currentURL = window.location;
      window.location = "http://140.114.77.15:"+currentURL.port+"/index";
    },
    error:function(error){
      console.log(error);
    }
  });
}