/* PythonKitchen — minimal, dependency-free enhancements.
 * Each feature is independent and guarded so a missing element never breaks another. */
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. Theme (dark mode as a designed surface) ---------- */
  (function theme() {
    var ROOT = document.documentElement;
    var KEY = 'pk-theme';
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) {}
    var systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var dark = stored ? stored === 'dark' : systemDark;
    ROOT.classList.toggle('dark', dark);

    var btns = $$('[data-theme-toggle]');
    if (!btns.length) return;
    var sync = function () {
      var isDark = ROOT.classList.contains('dark');
      btns.forEach(function (b) {
        b.setAttribute('aria-pressed', String(isDark));
        b.setAttribute('title', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      });
    };
    sync();
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var isDark = ROOT.classList.toggle('dark');
        try { localStorage.setItem(KEY, isDark ? 'dark' : 'light'); } catch (e) {}
        sync();
      });
    });
    // React to system changes when the user hasn't chosen explicitly.
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
      if (stored) return;
      ROOT.classList.toggle('dark', e.matches);
      sync();
    });
  })();

  /* ---------- 2. Mobile nav ---------- */
  (function mobileNav() {
    var btn = $('[data-nav-toggle]');
    var menu = $('#mobile-menu');
    if (!btn || !menu) return;
    var open = false;
    var set = function (v) {
      open = v;
      menu.classList.toggle('hidden', !open);
      btn.setAttribute('aria-expanded', String(open));
    };
    btn.addEventListener('click', function () { set(!open); });
    $$('#mobile-menu a').forEach(function (a) {
      a.addEventListener('click', function () { set(false); });
    });
  })();

  /* ---------- 3. Reading progress bar ---------- */
  (function progress() {
    var bar = $('#reading-progress');
    if (!bar) return;
    var tick = function () {
      var h = document.documentElement;
      var max = (h.scrollHeight - h.clientHeight) || 1;
      var p = Math.min(1, Math.max(0, (h.scrollTop || document.body.scrollTop) / max));
      bar.style.transform = 'scaleX(' + p + ')';
    };
    tick();
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
  })();

  /* ---------- 4. Scroll reveal (functional, motion-aware) ---------- */
  (function reveal() {
    var els = $$('[data-reveal]');
    if (!els.length || reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('reveal-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('reveal-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });
    els.forEach(function (el) { io.observe(el); });
  })();

  /* ---------- 5. Article: heading anchors + copy link ---------- */
  (function anchors() {
    var art = $('article.prose');
    if (!art) return;
    var heads = $$('h1, h2, h3', art);
    heads.forEach(function (h) {
      if (h.id) return;
      var id = (h.textContent || '').toLowerCase().trim()
        .replace(/[^\w\s-]/g, '').replace(/\s+/g, '-').slice(0, 80);
      if (!id) return;
      h.id = id;
    });
    $$('h1, h2, h3', art).forEach(function (h) {
      if (!h.id || h.querySelector('.anchor')) return;
      var a = document.createElement('a');
      a.className = 'anchor';
      a.href = '#' + h.id;
      a.setAttribute('aria-label', 'Copy link to this section');
      a.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>';
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var url = location.origin + location.pathname + '#' + h.id;
        if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { flash(a, 'Link copied!'); });
        history.replaceState(null, '', '#' + h.id);
      });
      h.appendChild(a);
    });

    function flash(el, msg) {
      var t = document.createElement('span');
      t.className = 'anchor-toast';
      t.textContent = msg;
      el.appendChild(t);
      setTimeout(function () { if (t.parentNode) t.parentNode.removeChild(t); }, 1400);
    }
  })();

  /* ---------- 6. Table of contents + active highlight ---------- */
  (function toc() {
    var nav = $('#toc');
    if (!nav) return;
    var art = $('article.prose');
    if (!art) return;
    var items = $$('a[data-toc]', nav);
    if (!items.length) return;
    var byId = {};
    items.forEach(function (a) { byId[a.getAttribute('data-toc')] = a; });
    var heads = $$('h1, h2, h3', art).filter(function (h) { return h.id && byId[h.id]; });
    if (!heads.length) return;

    var active = null;
    var setActive = function (id) {
      if (active === id) return;
      active = id;
      items.forEach(function (a) {
        var on = a.getAttribute('data-toc') === id;
        a.classList.toggle('toc-active', on);
        if (on) {
          var el = a.parentElement;
          if (el && a.offsetParent) {
            var r = a.getBoundingClientRect();
            var pr = a.offsetParent.getBoundingClientRect();
            var top = a.offsetParent.scrollTop + r.top - pr.top - a.offsetParent.clientHeight / 2 + r.height / 2;
            a.offsetParent.scrollTop = Math.max(0, top);
          }
        }
      });
    };

    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) setActive(en.target.id);
      });
    }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });
    heads.forEach(function (h) { io.observe(h); });
  })();
})();
