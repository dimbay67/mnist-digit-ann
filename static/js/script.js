function predict() {
    
    // get canvas element from html
    canvas = document.getElementById("sheet");
    w = canvas.width;
    h = canvas.height;

    // get canvas 2D context
    ctx = canvas.getContext("2d");

    // get all pixel from images and convert to json
    let imgData = ctx.getImageData(0, 0, w, h);
    json = JSON.stringify(imgData.data);

    // create XHR object
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/predict";

    // open connection
    xhr.open("POST", url, true);

    // set request header
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert(this.responseText); // print prediction
        }
    };

    // send data with request
    xhr.send(json);

}

window.onload = function() {

    // create fabric canvas
    var canvas = new fabric.Canvas("sheet");

    // setting for canvas
    canvas.freeDrawingBrush.color = "#ffffff";
    canvas.freeDrawingBrush.width = 10;

    // turn on drawing mode
    canvas.isDrawingMode = true;
    
}