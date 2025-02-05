chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.stress_level && message.stress_level > 0.7) {  
        chrome.notifications.create({
            type: "basic",
            iconUrl: "assets/icon48.png",
            title: "Take a Break!",
            message: "Your stress level is high. Take a short break or try deep breathing.",
            buttons: [{ title: "Take a Break" }, { title: "Ignore" }]
        });
    }
    sendResponse({ received: true });
});

// Check stress level from storage periodically
function checkStoredStressLevel() {
    chrome.storage.local.get(["stress_level"], function (data) {
        if (data.stress_level >= 2) {
            chrome.notifications.create({
                type: "basic",
                iconUrl: "assets/icon128.png",
                title: "Take a Break!",
                message: "You seem stressed. Take a short break to relax.",
                priority: 2
            });
        }
    });
}

// Run periodically to check stress level
setInterval(checkStoredStressLevel, 60000); // Check every 60 seconds
