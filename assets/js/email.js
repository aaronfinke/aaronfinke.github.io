// Builds the mailto: address on click so it never sits in the page source for scrapers.
// See _includes/email.html.
document.addEventListener('click', function (ev) {
  var a = ev.target.closest && ev.target.closest('a.js-email');
  if (!a) return;
  var rev = function (s) { return s.split('').reverse().join(''); };
  var addr = rev(a.dataset.u) + '@' + rev(a.dataset.d);
  a.href = 'mailto:' + addr;
  if (a.hasAttribute('data-reveal') && !a.dataset.shown) {
    ev.preventDefault();               // first click: just show it
    a.textContent = addr;
    a.dataset.shown = '1';
    a.removeAttribute('title');
  }
  // otherwise the default action follows the freshly set mailto: href
});
