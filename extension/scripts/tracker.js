let lastKeyPressTime = null;
let keyIntervals = [];
let lastMouseMoveTime = null;
let mouseSpeeds = [];

// Capture keyboard activity
document.addEventListener("keydown", function (event) {
    let currentTime = new Date().getTime();
    if (lastKeyPressTime) {
        let interval = currentTime - lastKeyPressTime;
        keyIntervals.push(interval);  // Store time between key presses
    }
    lastKeyPressTime = currentTime;
});

// Capture mouse movement speed
document.addEventListener("mousemove", function (event) {
    let currentTime = new Date().getTime();
    if (lastMouseMoveTime) {
        let speed = currentTime - lastMouseMoveTime;
        mouseSpeeds.push(speed);
    }
    lastMouseMoveTime = currentTime;
});

// Send data to backend every 60 seconds
setInterval(() => {
    if (keyIntervals.length > 0 && mouseSpeeds.length > 0) {
        let avgTypingSpeed = keyIntervals.length / 60; // Keystrokes per second
        let avgHesitationTime = keyIntervals.reduce((a, b) => a + b, 0) / keyIntervals.length;
        let avgMouseSpeed = mouseSpeeds.reduce((a, b) => a + b, 0) / mouseSpeeds.length;

        let data = {
            typing_speed: avgTypingSpeed,
            hesitation_time: avgHesitationTime,
            mouse_speed: avgMouseSpeed
        };

        fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            chrome.runtime.sendMessage({ stress_level: result.stress_level });
        });

        keyIntervals = [];
        mouseSpeeds = [];
    }
}, 60000);  // Runs every 60 seconds
