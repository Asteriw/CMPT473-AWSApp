document.getElementById("if-part").addEventListener("click", logoutAPI(localStorage.getItem("access_token")), true);

var logoutAPI = (token)=>{
    
    var raw = JSON.stringify({"access_token":token});
    // create a JSON object with parameters for API call and store in a variable
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    let access_token = "";
    // make API call with parameters and use promises to get response
    let res = fetch("https://91ru9w2qqj.execute-api.us-east-1.amazonaws.com/dev", requestOptions)
    res.then(function(result){
        // console.log(result.body);
        // if(result.status == "200"){
        //   alert("log in Success");
        // }
        return result.json();
    }).then(function(data){
        console.log(data)
        // console.log(data["data"]["access_token"]);
        if(data["success"] == true){
        alert("Successfully logged out!")
        }
    })
    
}