const form = document.querySelector("#trip-form");
const note = document.querySelector("#form-note");
const submitButton = form.querySelector("button[type=submit]");
const inbox = "ryanhocking@gmail.com";
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
        _url: "https://forevermemoriestravel.com/",
      }),
    });
    const result = await response.json().catch(() => ({}));
    const message = String(result.message || "");
    const accepted = response.ok && String(result.success) === "true";
    if (accepted) {
      form.reset();
      note.textContent = "Sent. We have your request.";
    } else if (/activat/i.test(message)) {
      form.reset();
      note.textContent = "Received. We will get this request after the form address is confirmed once.";
    } else {
      note.textContent = "The request was not sent. Please try again.";
    }
  } catch (error) {
    note.textContent = "The request was not sent. Please try again.";
  } finally {
    submitButton.disabled = false;
  }
});
