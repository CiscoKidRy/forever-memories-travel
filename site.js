const form = document.querySelector("#trip-form");
const note = document.querySelector("#form-note");
const inbox = "ryanhocking@gmail.com";

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (form.company.value) {
    return;
  }
  const data = new FormData(form);
  const lines = [
    "Trip request from ForeverMemoriesTravel.rshocking.com",
    "",
    `Name: ${data.get("name")}`,
    `Email: ${data.get("email")}`,
    `Phone: ${data.get("phone") || ""}`,
    `Trip: ${data.get("trip")}`,
    `When: ${data.get("when") || ""}`,
    `Who is going: ${data.get("who") || ""}`,
    "",
    String(data.get("notes") || ""),
  ];
  const href = `mailto:${inbox}?subject=${encodeURIComponent("Trip request — Forever Memories Travel")}&body=${encodeURIComponent(lines.join("\n"))}`;
  note.textContent = `If your email app does not open, send this request to ${inbox}.`;
  window.location.href = href;
});
