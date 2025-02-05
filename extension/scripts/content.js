let script = document.createElement('script');
script.src = chrome.runtime.getURL('scripts/tracker.js');
document.documentElement.appendChild(script);
