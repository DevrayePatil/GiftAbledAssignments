// The same idea as your Python Library class,
// written in JavaScript so the page can use it.
let books = [
  { title: "Wings of Fire", author: "Kalam", copies: 2 },
  { title: "The Alchemist", author: "Coelho", copies: 1 },
  { title: "Ikigai", author: "Garcia", copies: 4 },
];
// ---- add a book (same merge rule as your Python add_book) ----
function addBook() {
  const title = document.getElementById("t").value.trim();
  const author = document.getElementById("a").value.trim();
  const copies = Number(document.getElementById("c").value);
  if (title === "" || author === "") {
    alert("Please fill in the title and the author.");
    return;
  }
  const existing = findBook(title);
  if (existing) {
    existing.copies = existing.copies + copies;
  } else {
    books.push({ title: title, author: author, copies: copies });
  }
  document.getElementById("t").value = "";
  document.getElementById("a").value = "";
  document.getElementById("c").value = 1;
  draw();
}
// ---- find a book, ignoring capital letters ----
function findBook(title) {
  for (let b of books) {
    if (b.title.toLowerCase() === title.toLowerCase()) {
      return b;
    }
  }
  return null;
}
// ---- borrow and return ----
function borrow(title) {
  const b = findBook(title);
  if (b.copies > 0) {
    b.copies = b.copies - 1;
  }
  draw();
}
function returnBook(title) {
  const b = findBook(title);
  b.copies = b.copies + 1;
  draw();
}
// ---- put everything on the screen ----
function draw() {
  const shelf = document.getElementById("shelf");

  shelf.innerHTML = "";
  let totalCopies = 0;
  for (let b of books) {
    totalCopies = totalCopies + b.copies;
    const card = document.createElement("div");
    card.className = "book";
    card.innerHTML =
      "<h3>" +
      b.title +
      "</h3>" +
      "<p class='author'>by " +
      b.author +
      "</p>" +
      "<p class='count'>" +
      b.copies +
      " available</p>" +
      "<button onclick=\"borrow('" +
      b.title +
      "')\">Borrow</button> " +
      "<button onclick=\"returnBook('" +
      b.title +
      "')\">Return</button>";
    shelf.appendChild(card);
  }
  document.getElementById("titleCount").textContent = books.length;
  document.getElementById("copyCount").textContent = totalCopies;


  
}
// draw once when the page opens
draw();
