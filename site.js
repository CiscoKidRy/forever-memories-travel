const form = document.querySelector("#trip-form");
const note = document.querySelector("#form-note");
const submitButton = form.querySelector("button[type=submit]");
const inbox = "jenniferr@dreamstravelconsulting.com";
const endpoint = `https://formsubmit.co/ajax/${inbox}`;

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (form.company.value) {
    return;
  }

  const data = new FormData(form);
  const email = String(data.get("email") || "");
  submitButton.disabled = true;
  note.textContent = "Sending your request…";

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        name: data.get("name"),
        email,
        phone: data.get("phone") || "",
        trip: data.get("trip"),
        when: data.get("when") || "",
        who: data.get("who") || "",
        message: data.get("notes") || "",
        _replyto: email,
        _subject: "Trip request — Forever Memories Travel",
        _template: "table",
        _captcha: "false",
        _url: "https://forevermemoriestravel.rshocking.com/",
      }),
    });
    const result = await response.json().catch(() => ({}));
    const message = String(result.message || "");
    const accepted = response.ok && String(result.success) === "true";
    if (accepted) {
      form.reset();
      note.textContent = "Sent. Jennifer Ramirez has your request.";
    } else if (/activat/i.test(message)) {
      form.reset();
      note.textContent = "Received. Jennifer Ramirez will get this request after she confirms the form once.";
    } else {
      note.textContent = `The request was not sent. Write to Jennifer Ramirez at ${inbox}.`;
    }
  } catch (error) {
    note.textContent = `The request was not sent. Write to Jennifer Ramirez at ${inbox}.`;
  } finally {
    submitButton.disabled = false;
  }
});
