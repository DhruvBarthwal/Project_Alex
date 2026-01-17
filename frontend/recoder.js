navigator.mediaDevices.getUserMedia({audio : True})
.then(stream=>{
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.ondataavailable = async e => {
        const blob = e.data;
    };
});