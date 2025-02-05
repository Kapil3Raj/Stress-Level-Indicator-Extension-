document.addEventListener("DOMContentLoaded", function () {
    fetchStressData();
});

function fetchStressData() {
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            typing_speed: Math.floor(Math.random() * 100),
            hesitation_time: (Math.random() * 2).toFixed(2),
            mouse_speed: Math.floor(Math.random() * 200)
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("stressIndicator").textContent = `Stress Level: ${data.stress_level}`;
        
        // Store stress level
        chrome.storage.local.set({ stress_level: data.stress_level });

        // Send message to background script
        chrome.runtime.sendMessage({ stress_level: data.stress_level });
    })
    .catch(error => {
        console.error("Error fetching stress level:", error);
        document.getElementById("stressIndicator").textContent = "Error fetching data.";
    });
}
