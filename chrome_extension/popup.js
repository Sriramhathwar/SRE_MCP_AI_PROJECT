document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("sendBtn").addEventListener("click", ask);

  document.getElementById("q").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
      ask();
    }
  });

});

async function ask() {
  const input = document.getElementById("q");
  const query = input.value;
  console.log("Sending query:", query);
  addMessage(query, "user");
  input.value = "";

  const res = await fetch("http://127.0.0.1:5000/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query})
  });
  console.log("Response status:", res.status);
  const data = await res.json();
  console.log("Response data:", data); 
  addMessage(data.answer, "bot");
}

function addMessage(text, type) {
  const chat = document.getElementById("chat");

  const div = document.createElement("div");
  div.className = type;
  div.innerText = text;

  chat.appendChild(div);
}