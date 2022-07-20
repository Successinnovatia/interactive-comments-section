var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        const response = JSON.parse(xhttp.responseText);
        let output = '';
        let myComments = response.comments;

        for (let i = 0; i<myComments.length; i++){
            output+= `<li>${response.comments[i].user.username}</li>`
        }
        document.getElementById('names').innerHTML = output;
        

    // console.log(response.comments[1].user.username);

    }
};
xhttp.open("GET", "data.json", true);
xhttp.send(); 