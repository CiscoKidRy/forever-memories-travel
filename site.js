const form = document.querySelector("#trip-form");
const note = document.querySelector("#form-note");
const submitButton = form.querySelector("button[type=submit]");
const endpoint = "https://inquiries.forevermemoriestravel.com/inquiries";
const buttonLabel = submitButton.textContent;
let locked = false;
let attempt = { material: "", key: "" };

function payloadMaterial(body) {
  return JSON.stringify(body);
}

function attemptKey(body) {
  const material = payloadMaterial(body);
  if (attempt.material !== material) {
    attempt = { material, key: crypto.randomUUID() };
  }
  return attempt.key;
}

function lockButton() {
  locked = true;
  submitButton.disabled = true;
  submitButton.textContent = "Sending your request…";
  submitButton.classList.add("is-pending");
  form.setAttribute("aria-busy", "true");
  note.textContent = "";
  note.setAttribute("role", "status");
}

function unlockButton(message) {
  locked = false;
  submitButton.disabled = false;
  submitButton.textContent = buttonLabel;
  submitButton.classList.remove("is-pending");
  form.removeAttribute("aria-busy");
  note.setAttribute("role", "alert");
  note.textContent = message;
  submitButton.focus();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (locked) {
    return;
  }
  if (form.company.value) {
    return;
  }
  if (!form.reportValidity()) {
    return;
  }

  const body = {
    name: form.name.value,
    email: form.email.value,
    phone: form.phone.value,
    trip: form.trip.value,
    when: form.when.value,
    who: form.who.value,
    notes: form.notes.value,
    company: form.company.value,
    source_url: `${location.origin}${location.pathname}`,
  };
  body.idempotency_key = attemptKey(body);
  lockButton();

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(body),
    });
    const result = await response.json().catch(() => ({}));
    if (response.status === 201 && result.id) {
      const mail = result.visitor_email === "sent" ? "sent" : "failed";
      window.location.assign(`thanks.html?ref=${encodeURIComponent(result.id)}&mail=${mail}`);
      return;
    }
    if (response.status === 409) {
      attempt = { material: "", key: "" };
    }
    const message = response.status === 429
      ? "We already have several requests from this network. Please wait and try again."
      : "The request was not sent. Please try again.";
    unlockButton(message);
  } catch (error) {
    unlockButton("The request was not sent. Please try again.");
  }
});
