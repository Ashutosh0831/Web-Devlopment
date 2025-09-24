const form = document.getElementById("contactForm");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const purpose = document.getElementById("purpose").value.trim();

  if (!email) return; // Use email as unique key

  let contacts = JSON.parse(localStorage.getItem("contacts")) || {};

  // Store securely without displaying
  contacts[email] = { name, email, phone, purpose };
  localStorage.setItem("contacts", JSON.stringify(contacts));

  form.reset();
});
