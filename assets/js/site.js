// Small enhancements; every page works without this file.
(function () {
  // Abstract toggles on paper entries
  var toggles = Array.prototype.slice.call(document.querySelectorAll('.abstract-toggle'));

  function setOpen(btn, open) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.setAttribute('aria-expanded', String(open));
    panel.classList.toggle('is-open', open);
  }

  toggles.forEach(function (btn) {
    btn.addEventListener('click', function () {
      setOpen(btn, btn.getAttribute('aria-expanded') !== 'true');
      syncAllButton();
    });
  });

  // "Show all abstracts" control on the research page
  var allBtn = document.querySelector('[data-toggle-all]');

  function syncAllButton() {
    if (!allBtn) return;
    var allOpen = toggles.length > 0 && toggles.every(function (b) {
      return b.getAttribute('aria-expanded') === 'true';
    });
    allBtn.setAttribute('aria-pressed', String(allOpen));
    allBtn.querySelector('span').textContent = allOpen ? 'Hide all abstracts' : 'Show all abstracts';
  }

  if (allBtn) {
    allBtn.hidden = false;
    allBtn.addEventListener('click', function () {
      var open = allBtn.getAttribute('aria-pressed') !== 'true';
      toggles.forEach(function (b) { setOpen(b, open); });
      syncAllButton();
    });
  }

  // Arriving via a link like /#deduct: open that paper's abstract and scroll to it
  if (location.hash) {
    var target = document.getElementById(location.hash.slice(1));
    var btn = target && target.classList.contains('paper') && target.querySelector('.abstract-toggle');
    if (btn) setOpen(btn, true);
    if (target) {
      requestAnimationFrame(function () {
        target.scrollIntoView({ block: 'start', behavior: 'instant' });
      });
    }
  }

  // Copy-to-clipboard buttons
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.querySelector('span');
    var original = label.textContent;
    btn.addEventListener('click', function () {
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(function () {
        label.textContent = 'Copied';
        setTimeout(function () { label.textContent = original; }, 1600);
      }).catch(function () {});
    });
  });
})();
