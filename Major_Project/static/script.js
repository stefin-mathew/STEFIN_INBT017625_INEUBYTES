async function sendMessage() {

    const input = document.getElementById("user-input");

    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Display user message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = message;

    chatBox.appendChild(userDiv);

    // Send message to Flask backend
    const response = await fetch("/respond", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const data = await response.json();

    // Display bot response
    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.textContent = data.response;

    chatBox.appendChild(botDiv);

    // Clear input box
    input.value = "";

    // Scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message when Enter key is pressed
document.getElementById("user-input").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});
