"use strict";

document.addEventListener("DOMContentLoaded", function () {
  fetchBooks();
  console.log("DOM READY");

  document
    .getElementById("bookForm")
    .addEventListener("submit", async function (event) {
      event.preventDefault();

      const formData = new FormData(event.target);
      const formDataObj = Object.fromEntries(formData.entries());

      const response = await fetch("/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams(formDataObj),
      });

      if (response.ok) {
        fetchBooks();
        event.target.reset();
      }
    });
});

const fetchBooks = async () => {
  const response = await fetch("http://localhost:8000/books", {
    method: "get",
    headers: { "content-type": "application/json" },
  });
  const data = await response.json();
  // fetchBooks(data[0]);
  const tableBody = document.querySelector("#booksTableBody");
  tableBody.innerHTML = "";
  data.forEach((book) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${book.id}</td>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.rating}</td>
          `;
    tableBody.appendChild(row);
  });
};

