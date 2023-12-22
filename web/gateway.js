async function startApp() {
    const videoFeed = document.getElementById('video-feed');
    await eel.init()();

    eel.expose(updateVideoFeed);

    function updateVideoFeed(imageData) {
        videoFeed.src = 'data:image/jpeg;base64,' + imageData;
    }
}

startApp();