// window.onload = function() {
//     document.getElementById("if-part").addEventListener("click", logoutAPI(localStorage.getItem("access_token")), true);
// }
var logoutAPI = (token)=>{
    console.log("Logging out")
    // instantiate a headers object
    var myHeaders = new Headers();
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
    let res = fetch("https://6yya32xzii.execute-api.us-east-1.amazonaws.com/dev", requestOptions)
    res.then(function(result){
        // console.log(result.body);
        // if(result.status == "200"){
        //   alert("log in Success");
        // }
        return result.json();
    })
}