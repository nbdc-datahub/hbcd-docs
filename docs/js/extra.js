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
// Converts a copy-box's rendered HTML into a plain-text version that inlines
// link URLs as "text (href)" instead of silently dropping them, since plain
// innerText/textContent only keeps a link's visible label.
function copyBoxNodeToPlainText(node) {
  let result = "";
  node.childNodes.forEach(function (child) {
      if (child.nodeType === Node.TEXT_NODE) {
          result += child.textContent;
      } else if (child.nodeType === Node.ELEMENT_NODE) {
          const tag = child.tagName.toLowerCase();
          if (tag === "a" && child.href) {
              const linkText = copyBoxNodeToPlainText(child).trim();
              result += linkText === child.href ? linkText : `${linkText} (${child.href})`;
          } else if (tag === "br") {
              result += "\n";
          } else if (tag === "p" || tag === "div" || tag === "li" || /^h[1-6]$/.test(tag)) {
              result += copyBoxNodeToPlainText(child).trim() + "\n\n";
          } else {
              result += copyBoxNodeToPlainText(child);
          }
      }
  });
  return result;
}

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".copy-button").forEach(function (button) {
      button.addEventListener("click", function () {
          // Prefer an explicit data-copy-target id (needed when md_in_html wraps the
          // button in its own <p>, breaking the previousElementSibling relationship);
          // fall back to the sibling element for simpler, non-Markdown usages.
          const targetId = this.dataset.copyTarget;
          const source = targetId ? document.getElementById(targetId) : this.previousElementSibling;
          if (!source) {
              button.textContent = "Error";
              return;
          }

          const plainText = copyBoxNodeToPlainText(source).trim().replace(/\n{3,}/g, "\n\n");
          const markCopied = () => {
              button.textContent = "Copied!";
              setTimeout(() => (button.textContent = "Copy"), 2000);
          };
          const markError = () => {
              button.textContent = "Error";
          };

          if (navigator.clipboard.write && window.ClipboardItem) {
              // Write both flavors so pasting into a rich-text editor (Word, Google Docs,
              // email) keeps real clickable links, while a plain-text paste still gets
              // the URLs inlined via copyBoxNodeToPlainText above.
              const item = new ClipboardItem({
                  "text/plain": new Blob([plainText], { type: "text/plain" }),
                  "text/html": new Blob([source.innerHTML], { type: "text/html" }),
              });
              navigator.clipboard.write([item]).then(
                  markCopied,
                  () => navigator.clipboard.writeText(plainText).then(markCopied, markError)
              );
          } else {
              navigator.clipboard.writeText(plainText).then(markCopied, markError);
          }
      });
  });
});


// Color pills along a light -> dark shade of the site's blue (#199bd6),
// ordered by the numeric version embedded in each pill's value
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
