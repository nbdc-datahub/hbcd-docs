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


// Color pills along a light -> dark shade of the site's blue (#199bd6),
// ordered by the numeric version embedded in each pill's value
// (e.g. "30.1" -> 30.1, "R3.0" -> 3.0), so color tracks progression
// rather than being pseudo-random per value.
const PILL_GRADIENT_HUE = 199;
const PILL_GRADIENT_SATURATION = 79;
const PILL_GRADIENT_LIGHTNESS_START = 75; // light blue
const PILL_GRADIENT_LIGHTNESS_END = 25;   // dark blue

function pillSortKey(value) {
  const match = value.match(/[\d.]+/);
  return match ? parseFloat(match[0]) : null;
}

function colorForRank(t) {
  const lightness = PILL_GRADIENT_LIGHTNESS_START +
    (PILL_GRADIENT_LIGHTNESS_END - PILL_GRADIENT_LIGHTNESS_START) * t;
  return `hsl(${PILL_GRADIENT_HUE}, ${PILL_GRADIENT_SATURATION}%, ${lightness}%)`;
}

const pills = document.querySelectorAll('.pill');
const values = Array.from(pills, pill => pill.textContent.trim());

const orderedValues = Array.from(new Set(values))
  .filter(value => pillSortKey(value) !== null)
  .sort((a, b) => pillSortKey(a) - pillSortKey(b));

const colorByValue = new Map();
orderedValues.forEach((value, index) => {
  const t = orderedValues.length > 1 ? index / (orderedValues.length - 1) : 0.5;
  colorByValue.set(value, colorForRank(t));
});

pills.forEach(pill => {
  const value = pill.textContent.trim();
  pill.style.backgroundColor = colorByValue.get(value) || '#888';
});


// Search menu on known issues page
