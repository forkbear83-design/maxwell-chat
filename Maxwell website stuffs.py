<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Maxwell Chat</title>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #0f172a;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
#chat-container {
  width: 95%;
  max-width: 480px;
  height: 90vh;
  background-color: #020617;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  padding: 10px;
}
#messages {
  flex: 1;
  overflow-y: auto;
  padding: 5px;
}
.msg {
  margin: 6px 0;
}
.user { color: #38bdf8; }
.bot { color: #a5b4fc; }
#input-container {
  display: flex;
  margin-top: 5px;
}
#input {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: none;
  font-size: 16px;
}
#send, #reset {
  margin-left: 5px;
  padding: 12px 16px;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
}
#send { background-color: #38bdf8; color: black; }
#reset { background-color: #f87171; color: black; }
</style>
</head>
<body>

<div id="chat-container">
  <div id="messages"></div>
  <div id="input-container">
    <input id="input" placeholder="Talk to Maxwell..." autofocus>
    <button id="send">Send</button>
    <button id="reset">Reset Chat</button>
  </div>
</div>

<script>
const messages = document.getElementById("messages");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");
const resetBtn = document.getElementById("reset");

let mood = "happy";
let learnedJokes = [];
let learnedFacts = [];

const faces = {
  happy: [":)", ":D", ":3"],
  sad: [":(", ":'("],
  playful: [";)", ":P", ":3"],
  angry: [">:("],
  curious: [":o", "o_o"]
};

const jokes = [
  "Why do programmers hate nature? Too many bugs :)",
  "Why was the computer cold? It left its Windows open :)",
  "Why did the scarecrow win an award? He was outstanding in his field :)"
];

const facts = [
  "Honey never spoils.",
  "Octopuses have three hearts.",
  "Bananas are berries, but strawberries are not.",
  "Sharks existed before trees.",
  "A group of flamingos is called a flamboyance."
];

function face() {
  // 50% chance to show a face
  if (Math.random() < 0.5) return faces[mood][Math.floor(Math.random() * faces[mood].length)];
  return "";
}

function say(text, cls) {
  const div = document.createElement("div");
  div.className = "msg " + cls;
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function handleMessage(text) {
  const t = text.toLowerCase();

  // Mood detection
  if (["sad","lonely","tired"].some(w => t.includes(w))) mood = "sad";
  if (["happy","great","love"].some(w => t.includes(w))) mood = "happy";
  if (["angry","mad","hate"].some(w => t.includes(w))) mood = "angry";
  if (["joke","fun"].some(w => t.includes(w))) mood = "playful";
  if (["why","how","what"].some(w => t.includes(w))) mood = "curious";

  // Learning
  if (t.startsWith("learn joke")) {
    learnedJokes.push(text.slice(10).trim());
    say("Maxwell: I learned a new joke! " + face(), "bot");
    return;
  }
  if (t.startsWith("learn fact")) {
    learnedFacts.push(text.slice(10).trim());
    say("Maxwell: I learned a new fact! " + face(), "bot");
    return;
  }

  // Responses
  if (t.includes("hello") || t.includes("hi")) {
    say("Maxwell: Hey! Nice to see you " + face(), "bot");
  }
  else if (t.includes("joke")) {
    const all = jokes.concat(learnedJokes);
    say("Maxwell: " + all[Math.floor(Math.random()*all.length)], "bot");
  }
  else if (t.includes("fact")) {
    const all = facts.concat(learnedFacts);
    say("Maxwell: Fun fact: " + all[Math.floor(Math.random()*all.length)] + " " + face(), "bot");
  }
  else if (t.includes("how are you")) {
    say("Maxwell: I feel " + mood + " " + face(), "bot");
  }
  else {
    const replies = [
      "Tell me more " + face(),
      "I’m listening " + face(),
      "That’s interesting " + face(),
      "Oh? Go on " + face()
    ];
    say("Maxwell: " + replies[Math.floor(Math.random()*replies.length)], "bot");
  }
}

// Event listeners
sendBtn.addEventListener("click", () => {
  const text = input.value.trim();
  if (!text) return;
  say("You: " + text, "user");
  input.value = "";
  handleMessage(text);
});

input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendBtn.click();
});

// Reset button
resetBtn.addEventListener("click", () => {
  messages.innerHTML = "";
  mood = "happy";
  learnedJokes = [];
  learnedFacts = [];
  say("Maxwell: Chat reset! Hello again " + face(), "bot");
});

// Welcome message
say("Maxwell: Hello! You can talk to me about anything " + face(), "bot");
</script>

</body>
</html>