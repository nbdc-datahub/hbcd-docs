// Collapsible content
function toggleNotificationCollapse(banner) {
  const content = banner.nextElementSibling;
  if (content && content.classList.contains('open-collapsible-content')) {
    content.classList.toggle('open');
  }
}

// Collapsed content: toggles open AND rotate to ON when arrow is clicked to expand/collapse the section.
function toggleCollapse(element) {
  const collapsibleContent = element.nextElementSibling;
  const arrow = element.querySelector(['.arrow']);

  if (collapsibleContent.classList.contains('open')) {
    collapsibleContent.classList.remove('open');
    arrow.classList.remove('rotate');
  } else {
    collapsibleContent.classList.add('open');
    arrow.classList.add('rotate');
  }
}

// Utility function to expand a collapsible section by ID
function expandCollapsibleById(id) {
  const element = document.getElementById(id);

  if (element && (element.classList.contains('banner'))) {
    const collapsibleContent = element.nextElementSibling;
    const arrow = element.querySelector(['.arrow']);
    if (collapsibleContent && !collapsibleContent.classList.contains('open')) {
      collapsibleContent.classList.add('open');
      if (arrow) arrow.classList.add('rotate');
    }
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

// Auto-expand banners if navigated via external link
document.addEventListener('DOMContentLoaded', function () {
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});

// Listen for hash changes to expand collapsible sections
window.addEventListener('hashchange', () => {
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});

// Click to copy 
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".copy-button").forEach(function (button) {
      button.addEventListener("click", function () {
          const textToCopy = this.previousElementSibling.textContent; // Get the text from the sibling element
          navigator.clipboard.writeText(textToCopy).then(
              () => {
                  button.textContent = "Copied!";
                  setTimeout(() => (button.textContent = "Copy"), 2000);
              },
              () => {
                  button.textContent = "Error";
              }
          );
      });
  });
});
