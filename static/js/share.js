document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("shareModal");
  const shareLinksContainer = document.getElementById("shareLinksContainer");
  const copyAllBtn = document.getElementById("copyAllBtn");
  const closeModal = document.getElementById("closeModal");
  const restrictedAccess = document.getElementById("restrictedAccess");
  const multiShareBtn = document.getElementById("multiShareBtn");
  const checkboxes = document.querySelectorAll(".file-checkbox");
  const singleShareButtons = document.querySelectorAll(".single-share-btn");
  function showShareModal(links) {
    if (links.length === 0) return;

    let baseURL = "http://127.0.0.1:8000/share/";
    let formattedLink = baseURL + links.join(",");

    shareLinksContainer.innerHTML = `<input type="text" class="w-full border p-2 rounded-lg" value="${formattedLink}" readonly>`;
    modal.classList.remove("hidden");
  }

  singleShareButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const fileUrl = this.getAttribute("data-file-url");
      showShareModal([fileUrl]);
    });
  });

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      const selectedFiles = [...checkboxes]
        .filter((c) => c.checked)
        .map((c) => c.getAttribute("data-file-url"));
      multiShareBtn.classList.toggle("hidden", selectedFiles.length === 0);
    });
  });

  multiShareBtn.addEventListener("click", function () {
    const selectedFiles = [...checkboxes]
      .filter((c) => c.checked)
      .map((c) => c.getAttribute("data-file-url"));
    showShareModal(selectedFiles);
  });

  copyAllBtn.addEventListener("click", function () {
    const links = [...shareLinksContainer.querySelectorAll("input")]
      .map((input) => input.value)
      .join("\n");
    navigator.clipboard
      .writeText(links)
      .then(() => alert("Links copied to clipboard!"));
  });

  closeModal.addEventListener("click", function () {
    modal.classList.add("hidden");
  });

  restrictedAccess.addEventListener("change", function () {
    const inputs = shareLinksContainer.querySelectorAll("input");
    inputs.forEach((input) => {
      if (this.checked) {
        input.value = input.value.includes("?auth=true")
          ? input.value
          : input.value + "?auth=true";
      } else {
        input.value = input.value.replace("?auth=true", "");
      }
    });
  });
});
