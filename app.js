var apiKey = "0fb41fe10d3141f68910857a7a54304b";
var apiUrl = "https://api.projectoxford.ai/emotion/v1.0/recognize";

var video = document.getElementById("videoElement");
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var photoBtn = $('#snap')
var moodBtn = $('#btn-get-mood')
var userFileBlob;
var userFileURL;

// ************************************* setup web cam ************************************* //

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;

if (navigator.getUserMedia) {       
    navigator.getUserMedia({video: true}, handleVideo, videoError);
}

// handle video success
function handleVideo(stream) {
    video.src = window.URL.createObjectURL(stream);
}

// handle video error
function videoError(e) {
    console.log("Video Error!");
}

// ************************************* add button listeners ************************************* //

// register "snap photo" button call back
photoBtn.click(function() {
    context.drawImage(video, 0, 0, 640, 480)
    userFileBlob = blobToFile(dataURItoBlob(canvas.toDataURL('image/jpeg', 1.0)), "file.jpg")
});

// register "get music" button call back
moodBtn.click(function () {
    getAzureEmotions(userFileBlob, apiUrl, apiKey);
});

// ************************************* Azure API Interaction ************************************* //

/**
 *
**/
function getAzureEmotions(file, apiUrl, apiKey)  {
    $.ajax({ // make ajax request
        url: apiUrl,
        beforeSend: function (xhrObj) {
            xhrObj.setRequestHeader("Content-Type", "application/octet-stream");
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", apiKey);
        },
        type: "POST",
        data: file,
        processData: false
    })
    .done(function (response) { // handle success 
        ProcessEmotions(response);
    })
    .fail(function (error) { // handle failure
        $("#results-window").text(error.getAllResponseHeaders());
    });
}

// azure success callback
function ProcessEmotions(response)    {
    // the response is of the form [{...}] if the array has length 0, no face is detected
    if (response.length < 1) {
        $("#results-window").text("Yo, thats not a face! bIshhhhh");    
    } else {
        // otherwise, a face was detected and display results for now
        var jsonObj = response[0]
        var text = "Now that's a face!\n" 
        var emotionScores = jsonObj.scores
        var maxEmotionScore = 0;
        var maxEmotion;
        
        // calculate max emotion score and emotion
        for (var emotion in emotionScores) {
            emotionScore = emotionScores[emotion];
            if (emotionScore >= maxEmotionScore) {
                maxEmotionScore = emotionScore 
                maxEmotion = emotion
            }
        }

        if (ProcessEmotions)

        text += "I'm " + (maxEmotionScore * 100.0).toFixed(2) + "% sure that your primary emotion is " + maxEmotion + "."

        // console.log(maxEmotion, maxEmotionScore)

        $("#results-window").text(text);
    }
}

[
{"faceRectangle":
    {"height":130,"left":302,"top":221,"width":130},
    "scores":
        {"anger":0.000147724684,"contempt":0.000356299279,"disgust":0.0002667001,"fear":0.000008582338,
        "happiness":0.0000459349,"neutral":0.9933396,"sadness":0.00572407246,"surprise":0.000111103378}
    }
]







function dataURItoBlob(dataURI) {
    // convert base64/URLEncoded data component to raw binary data held in a string
    var byteString;
    if (dataURI.split(',')[0].indexOf('base64') >= 0)
        byteString = atob(dataURI.split(',')[1]);
    else
        byteString = unescape(dataURI.split(',')[1]);

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to a typed array
    var ia = new Uint8Array(byteString.length);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }

    return new Blob([ia], {type:mimeString});
}

function blobToFile(theBlob, fileName){
    //A Blob() is almost a File() - it's just missing the two properties below which we will add
    theBlob.lastModifiedDate = new Date();
    theBlob.name = fileName;
    return theBlob;
}

