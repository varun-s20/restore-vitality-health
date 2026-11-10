/* ==========================================================================
   RestoreVitality Health: global script
   Loaded by every page with defer, after assets/global.css. Plain ES5, no libraries, no build step.
   Blocks: header states, menu drawer, hero load and zoom (from the approved prototype), current link,
   tabs, treatment rail drag, intro reveals, the How it works seam (pass 8b), the eased step stage, the category cover,
   sticky CTA, cookie notice, forms, quiz.
   Every block checks for its own markup first, so one file serves every page.
   window.SITE_FORM_ENDPOINT: the URL forms POST to (set by the host page or CMS). Unset, forms say so.
   ========================================================================== */
(function () {
  'use strict';

  /* ---- config and flags ---- */
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia('(hover: hover) and (any-pointer: fine)').matches;
  var STORE = 'rvh:';
  var root = document.documentElement;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function clamp(v, min, max) { return Math.min(max, Math.max(min, v)); }
  var raf = window.requestAnimationFrame.bind(window);

  /* ===== Scroll work: one passive listener, batched in rAF ===== */
  var scrollJobs = [];
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    raf(function () {
      ticking = false;
      for (var i = 0; i < scrollJobs.length; i++) scrollJobs[i]();
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ===== Header: frosted once the page moves; plum-on-cream over light bands =====
     A band marks itself with data-header-theme="light". The header reads which band sits
     under its middle line, so the logo never vanishes on a light ground. */
  (function () {
    var header = $('[data-header]');
    if (!header) return;
    var lightBands = $$('[data-header-theme="light"]');
    function update() {
      var y = window.pageYOffset;
      header.classList.toggle('is-scrolled', y > 8);
      var mid = header.offsetHeight / 2;
      var light = false;
      for (var i = 0; i < lightBands.length; i++) {
        var r = lightBands[i].getBoundingClientRect();
        if (r.top <= mid && r.bottom >= mid) { light = true; break; }
      }
      header.classList.toggle('is-light', light);
    }
    scrollJobs.push(update);
    update();
  })();

  /* ===== Submenus (Chateau Margaux): the bar becomes the panel =====
     Opens the moment the pointer enters a link (no hover delay), stays open anywhere inside the header, closes
     the moment it leaves. Moving between links swaps the content at once and only tweens the sheet's height.
     Keyboard: the link goes to its page; the chevron button beside it opens the panel (Enter or Space), Tab
     then walks into the cards, Escape closes and returns to the chevron, leaving the header closes. Tabbing
     across a closed bar is three stops. Margaux's own bar is mouse-only; this one is not. */
  (function () {
    var header = $('[data-header]');
    if (!header) return;
    var items = $$('[data-submenu]', header);
    if (!items.length) return;
    var current = null;
    var warmed = false;

    function warm() {
      /* the panel images are lazy; load them all on the first approach so nothing pops in */
      if (warmed) return;
      warmed = true;
      $$('.m-subnav img', header).forEach(function (img) { img.loading = 'eager'; });
    }
    function open(item) {
      if (current === item) return;
      warm();
      var swap = !!current;
      if (current) {
        current.classList.remove('is-open');
        $('[data-submenu-trigger]', current).setAttribute('aria-expanded', 'false');
      }
      current = item;
      /* already open: swap without a second curtain (CSS .is-swap) */
      item.classList.toggle('is-swap', swap);
      item.classList.add('is-open');
      $('[data-submenu-trigger]', item).setAttribute('aria-expanded', 'true');
      header.style.setProperty('--sub-h', $('[data-submenu-panel]', item).offsetHeight + 'px');
      header.classList.add('is-sub');
    }
    function close(returnFocus) {
      if (!current) return;
      var trigger = $('[data-submenu-trigger]', current);
      current.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
      header.classList.remove('is-sub');
      current = null;
      if (returnFocus) trigger.focus();
    }
    items.forEach(function (item) {
      var trigger = $('[data-submenu-trigger]', item);
      var link = $('[data-submenu-link]', item);
      [trigger, link].forEach(function (el) {
        el.addEventListener('mouseenter', function () { if (finePointer) open(item); });
      });
      trigger.addEventListener('click', function () {
        if (current === item) close(false); else open(item);
      });
      /* focusing another item's link closes an open panel, so keyboard and panel never disagree */
      link.addEventListener('focus', function () { if (current && current !== item) close(false); });
    });
    header.addEventListener('mouseleave', function () { if (finePointer) close(false); });
    header.addEventListener('focusout', function (e) {
      if (!e.relatedTarget || !header.contains(e.relatedTarget)) close(false);
    });
    /* the menu pill, the logo and the right side close it when focused, so only one panel story runs at a time */
    $$('.a-navPill, .o-header__logo, .o-header__side.-right a', header).forEach(function (el) {
      el.addEventListener('focus', function () { close(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && current) { e.preventDefault(); close(true); }
    });
    window.addEventListener('resize', function () { if (window.innerWidth < 1360) close(false); });
  })();

  /* ===== Menu drawer: a modal dialog =====
     Page goes inert, focus moves to Close, Tab stays inside, Escape closes,
     focus returns to the Menu button. */
  (function () {
    var menu = $('[data-menu]');
    var openBtn = $('[data-menu-open]');
    if (!menu || !openBtn) return;
    var panel = $('[data-menu-panel]', menu);
    var outside = [$('[data-header]'), $('#main'), $('.a-skipLink'), $('.o-footer'), $('[data-sticky-cta]'), $('[data-cookie]')].filter(Boolean);
    var lastFocus = null;

    function focusables() {
      return $$('a[href], button:not([disabled])', panel).filter(function (el) { return el.offsetParent !== null; });
    }
    function open() {
      lastFocus = document.activeElement;
      menu.classList.add('is-open');
      openBtn.setAttribute('aria-expanded', 'true');
      outside.forEach(function (el) { el.inert = true; });
      root.style.overflow = 'hidden';
      var first = $('[data-menu-close].a-navPill', panel);
      if (first) setTimeout(function () { first.focus(); }, reduceMotion ? 0 : 60);
      document.addEventListener('keydown', onKey);
    }
    function close() {
      menu.classList.remove('is-open');
      openBtn.setAttribute('aria-expanded', 'false');
      outside.forEach(function (el) { el.inert = false; });
      root.style.overflow = '';
      document.removeEventListener('keydown', onKey);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function onKey(e) {
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    openBtn.addEventListener('click', open);
    $$('[data-menu-close]', menu).forEach(function (el) { el.addEventListener('click', close); });
    /* a link to this same page closes the drawer instead of leaving it open */
    $$('a[href]', panel).forEach(function (a) { a.addEventListener('click', function () { if (menu.classList.contains('is-open')) close(); }); });
    /* back/forward cache: never come back to an open drawer */
    window.addEventListener('pageshow', function (e) { if (e.persisted && menu.classList.contains('is-open')) close(); });
  })();

  /* ===== Hero: load sequence =====
     Waits for the display font (or 1.2s at most) so the masked rows rise in their real shape, then adds
     is-loaded; CSS does the moving. Reduced motion shows everything at once. */
  (function () {
    var hero = $('[data-hero]');
    if (!hero) { root.classList.add('is-loaded'); return; }
    var done = false;
    function go() {
      if (done) return;
      done = true;
      window.requestAnimationFrame(function () { root.classList.add('is-loaded'); });
      /* the sequence ends at about 2.6s; from then on the exit curves apply (CSS .is-settled) */
      setTimeout(function () { root.classList.add('is-settled'); }, reduceMotion ? 0 : 2700);
    }
    if (reduceMotion) { go(); return; }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(go).catch(go);
    setTimeout(go, 1200);
  })();

  /* ===== Hero: Neko's scrub =====
     641 up: the stage is pinned (CSS, section 140svh) for .4 of a screen. Over the pin the frame closes in
     (--hp 0 to 1); the photo scales to 1.044 and softens to 1.5px over one screen.
     The copy is pinned with the stage. Neko's copy scrolls over its photo; here that would carry plum
     letters across his beard (1.2:1 sampled), so as soon as the visitor scrolls (24px) the headline rows
     and the lead leave through their own masks (CSS .is-leaving, time-based, .8s), and come back under 8px.
     The actions stay on the stage through the pin and leave with it.
     Phones (Neko at 390): no pin, copy and photo scroll away together; the photo scales to 1.05 and softens
     to 3px over .7 of a screen. */
  (function () {
    var wide = window.matchMedia('(min-width: 641px)');
    var hero = $('[data-hero]');
    if (!hero || reduceMotion) return;
    var img = $('[data-hero-img]', hero);
    var leaving = false;
    var last = -1;
    function update() {
      var y = Math.max(0, window.pageYOffset);
      var vh = window.innerHeight;
      if (y > vh * 1.8 && last > vh * 1.8) return;  /* off screen: nothing to write */
      last = y;
      if (wide.matches) {
        var pin = vh * 0.4;  /* --hero-pin; Neko's .75 left a long wordless stretch here (critic round 2) */
        var p = clamp(y / pin, 0, 1);
        var q = clamp(y / vh, 0, 1);
        hero.style.setProperty('--hp', p.toFixed(4));
        hero.style.setProperty('--hs', (1 + 0.044 * q).toFixed(4));
        hero.style.setProperty('--hb', (1.5 * q).toFixed(2) + 'px');
        if (!leaving && y > 24) { leaving = true; hero.classList.add('is-leaving'); }
        else if (leaving && y < 8) { leaving = false; hero.classList.remove('is-leaving'); }
      } else {
        var m = clamp(y / (vh * 0.7), 0, 1);
        hero.style.setProperty('--hp', '0');
        hero.style.setProperty('--hs', (1 + 0.05 * m).toFixed(4));
        hero.style.setProperty('--hb', (3 * m).toFixed(2) + 'px');
        if (leaving) { leaving = false; hero.classList.remove('is-leaving'); }
      }
    }
    if (img) img.style.willChange = 'transform, filter';
    scrollJobs.push(update);
    update();
  })();

  /* ===== Current page: aria-current on links to this page, read from the path (chrome is identical everywhere) ===== */
  (function () {
    var file = location.pathname.split('/').pop() || 'index.html';
    $$('.o-header a[href], .o-menu a[href], .o-footer a[href]').forEach(function (a) {
      if (a.getAttribute('href') === file && !a.closest('.m-langSwitch')) a.setAttribute('aria-current', 'page');
    });
  })();

  /* ===== Tabs: one pattern for the treatment rail, the FAQ and the pricing cards =====
     [data-tabs] holds role="tab" buttons with aria-controls. Arrow keys move between tabs (automatic
     activation). A group with data-tabs-class swaps that class instead of `hidden` (pricing: CSS shows every
     card from 1025, so the tabs only matter on smaller screens). */
  (function () {
    $$('[data-tabs]').forEach(function (list) {
      var tabs = $$('[role="tab"]', list);
      var useClass = list.getAttribute('data-tabs-class');
      list.hidden = false;
      function select(tab, focus) {
        tabs.forEach(function (t) {
          var on = t === tab;
          var panel = document.getElementById(t.getAttribute('aria-controls'));
          t.setAttribute('aria-selected', on ? 'true' : 'false');
          t.tabIndex = on ? 0 : -1;
          if (!panel) return;
          if (useClass) panel.classList.toggle(useClass, on);
          else panel.hidden = !on;
        });
        if (focus) tab.focus();
      }
      tabs.forEach(function (tab, i) {
        tab.addEventListener('click', function () { select(tab, false); });
        tab.addEventListener('keydown', function (e) {
          var n = null;
          if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
          else if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
          else if (e.key === 'Home') n = tabs[0];
          else if (e.key === 'End') n = tabs[tabs.length - 1];
          if (n) { e.preventDefault(); select(n, true); }
        });
      });
      var current = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0];
      select(current, false);
    });
  })();

  /* ===== Treatment rail: drag to scroll with a mouse (touch and trackpads scroll natively) ===== */
  (function () {
    if (!finePointer) return;
    $$('[data-rail]').forEach(function (rail) {
      var startX = 0, startLeft = 0, down = false, moved = false;
      rail.addEventListener('pointerdown', function (e) {
        if (e.pointerType !== 'mouse' || e.button !== 0) return;
        down = true; moved = false; startX = e.clientX; startLeft = rail.scrollLeft;
      });
      window.addEventListener('pointermove', function (e) {
        if (!down) return;
        var dx = e.clientX - startX;
        if (!moved && Math.abs(dx) > 6) { moved = true; rail.classList.add('is-dragging'); }
        if (moved) rail.scrollLeft = startLeft - dx;
      });
      window.addEventListener('pointerup', function () {
        if (!down) return;
        down = false;
        /* the click that ends a drag must not open a card */
        setTimeout(function () { rail.classList.remove('is-dragging'); }, 0);
      });
      rail.addEventListener('dragstart', function (e) { e.preventDefault(); });
    });
  })();

  /* ===== Intro reveals (spec 5, Margaux intros only): heading words rise once, the paragraph follows ===== */
  (function () {
    var heads = $$('[data-reveal]');
    if (!heads.length) return;
    if (reduceMotion || !('IntersectionObserver' in window)) {
      heads.forEach(function (h) { h.classList.add('is-inview'); });
      $$('[data-reveal-follow]').forEach(function (p) { p.classList.add('is-inview'); });
      return;
    }
    var count = 0;
    function split(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (child) {
        if (child.nodeType === 3) {
          var frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var s = document.createElement('span');
            s.className = 'm-word';
            s.style.setProperty('--i', count++);
            s.textContent = part;
            frag.appendChild(s);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1) {
          split(child);
        }
      });
    }
    heads.forEach(function (h) { count = 0; split(h); });
    var pending = heads.slice();
    function reveal(h) {
      if (h.classList.contains('is-inview')) return;
      h.classList.add('is-inview');
      var follow = h.parentNode && $('[data-reveal-follow]', h.parentNode);
      if (follow) follow.classList.add('is-inview');
      io.unobserve(h);
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) reveal(en.target); });
    }, { rootMargin: '0px 0px -40px 0px' });
    heads.forEach(function (h) { io.observe(h); });
    /* critic round 3 (qa.py): a fast scroll or a jump can carry a heading past the screen between two observer
       checks, so it never intersects and stays hidden. On every scroll frame, on load and on resize, anything whose
       top has reached the screen's lower edge, or already passed above it, is revealed too. */
    function sweep() {
      if (!pending.length) return;
      var lim = window.innerHeight - 40;
      pending = pending.filter(function (h) {
        if (h.getBoundingClientRect().top < lim) { reveal(h); return false; }
        return !h.classList.contains('is-inview');
      });
    }
    scrollJobs.push(sweep);
    window.addEventListener('load', sweep);
    window.addEventListener('resize', sweep);
    sweep();
  })();

  /* ===== How it works: the gold seam (pass 8b, the one signature motion) =====
     One gold line runs from step to step and draws itself as the steps scroll by; each step's chip turns gold
     when the line reaches it. Technique: a scroll-linked stroke draw (stroke-dashoffset from scroll position),
     rebuilt from The Protocole's step progress bar in the concept's own mark. Steps in one row are joined by
     low arches that rise into the drawings; stacked steps are joined down a rail in the gutter beside them
     (--seam-rail, px left of the chips). It never moves on its own, only with the scroll. Reduced motion gets
     the finished line and every chip lit, with no scroll work. Neko's fixed ground gradient keeps warming the
     band underneath; the line finishes about where the ground peaks. */
  (function () {
    var lists = $$('[data-seam]');
    if (!lists.length) return;
    var NS = 'http://www.w3.org/2000/svg';
    var LIFT = [64, 42, 84, 52];  /* arch heights in px, fitted to the drawings' horizon (y 318 of 377) */
    lists.forEach(function (list) {
      var steps = $$('.m-step', list);
      var chips = $$('.m-step__chip', list);
      if (chips.length < 2) return;
      var svg = document.createElementNS(NS, 'svg');
      svg.setAttribute('class', 'o-steps__seam');
      svg.setAttribute('aria-hidden', 'true');
      var path = document.createElementNS(NS, 'path');
      svg.appendChild(path);
      list.insertBefore(svg, list.firstChild);
      var total = 0, marks = [], horizontal = false, lastW = window.innerWidth, t;

      function build() {
        var box = list.getBoundingClientRect();
        var rail = parseFloat(getComputedStyle(list).getPropertyValue('--seam-rail')) || 8;
        var pts = chips.map(function (c) {
          var r = c.getBoundingClientRect();
          return { x: r.left - box.left + r.width / 2, y: r.top - box.top + r.height / 2, left: r.left - box.left };
        });
        horizontal = Math.abs(pts[pts.length - 1].y - pts[0].y) < 20;
        var d = 'M' + pts[0].x + ' ' + pts[0].y;
        var probe = document.createElementNS(NS, 'path');
        svg.appendChild(probe);
        marks = [0];
        for (var i = 1; i < pts.length; i++) {
          var a = pts[i - 1], b = pts[i];
          if (Math.abs(b.y - a.y) < 20) {
            var dx = b.x - a.x, h = LIFT[(i - 1) % LIFT.length];
            d += ' C' + (a.x + dx * 0.28) + ' ' + (a.y - h) + ' ' + (b.x - dx * 0.34) + ' ' + (b.y - h * 0.8) + ' ' + b.x + ' ' + b.y;
          } else {
            var x = Math.min(a.left, b.left) - rail, k = Math.min(24, Math.abs(a.x - x));
            d += ' H' + (x + k) + ' Q' + x + ' ' + a.y + ' ' + x + ' ' + (a.y + k) +
                 ' V' + (b.y - k) + ' Q' + x + ' ' + b.y + ' ' + (x + k) + ' ' + b.y + ' H' + b.x;
          }
          probe.setAttribute('d', d);
          marks.push(probe.getTotalLength());
        }
        svg.removeChild(probe);
        path.setAttribute('d', d);
        total = path.getTotalLength();
        path.style.strokeDasharray = total + ' ' + total;
        draw();
      }

      function draw() {
        if (!total) return;
        var p = 1;
        if (!reduceMotion) {
          var vh = window.innerHeight;
          var first = chips[0].getBoundingClientRect(), last = chips[chips.length - 1].getBoundingClientRect();
          /* one row: drawn while the chips climb from 96% to 62% of the screen (pass 8c: it finished at 40%,
             near the top, so most visitors never saw it end); stacked: the tip follows a reading line at 70% of
             the screen, chip to chip */
          p = horizontal ? (vh * 0.96 - first.top) / (vh * 0.34)
                         : (vh * 0.7 - first.top) / Math.max(1, last.top - first.top);
          p = clamp(p, 0, 1);
        }
        var len = total * p;
        path.style.strokeDashoffset = String(total - len);
        for (var i = 0; i < steps.length; i++) steps[i].classList.toggle('is-reached', len >= marks[i] - 1);
      }

      build();
      if (!reduceMotion) scrollJobs.push(draw);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(build).catch(function () {});
      window.addEventListener('load', build);
      window.addEventListener('resize', function () {
        if (window.innerWidth === lastW) return;  /* height-only changes are the mobile URL bar */
        clearTimeout(t);
        t = setTimeout(function () { lastW = window.innerWidth; build(); }, 150);
      });
    });
  })();

  /* ===== Word-lit statement (Neko): words go from .3 to full one at a time with the scroll =====
     Starts when the paragraph's top reaches 75% of the screen, ends when its bottom reaches 35%. */
  (function () {
    var el = $('[data-litwords]');
    if (!el || reduceMotion) return;
    var words = el.textContent.trim().split(/\s+/);
    el.textContent = '';
    var spans = words.map(function (w, i) {
      var s = document.createElement('span');
      s.className = 'm-litWord';
      s.textContent = w;
      el.appendChild(s);
      if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
      return s;
    });
    var lit = -1;
    function update() {
      var r = el.getBoundingClientRect();
      var vh = window.innerHeight;
      var start = vh * 0.75, end = vh * 0.35 - r.height;
      var q = clamp((start - r.top) / (start - end), 0, 1);
      var n = Math.round(q * spans.length);
      if (n === lit) return;
      lit = n;
      for (var i = 0; i < spans.length; i++) spans[i].classList.toggle('is-lit', i < n);
    }
    scrollJobs.push(update);
    update();
  })();

  /* ===== Eased scroll follower: one value glides toward the scroll on requestAnimationFrame =====
     (Varun, 10 Nov: the stage's stacking photos "need to be smoother".) The scroll only sets a target; every frame
     moves the value a time-based share of the way there (an exponential ease with time constant tau, so it settles
     the same at 60 or 120Hz), and wheel notches, trackpad flicks and keyboard jumps all land as one glide. The loop
     runs only while the value is still moving. read() and write() never read layout in the frame. jump() true:
     land at once (the visitor arrived from far away, nothing on screen would show the glide). */
  function follower(read, write, tau, jump) {
    var cur = null, running = false, last = 0;
    function tick(t) {
      var target = read();
      var dt = last ? Math.min(t - last, 64) : 16.7;
      last = t;
      if (cur === null || (jump && jump())) cur = target;
      else cur += (target - cur) * (1 - Math.exp(-dt / (tau * 1000)));
      if (Math.abs(target - cur) < 0.0003) cur = target;
      write(cur);
      if (cur !== target) raf(tick);
      else { running = false; last = 0; }
    }
    return {
      kick: function () { if (!running) { running = true; raf(tick); } },
      snap: function () { cur = read(); write(cur); }
    };
  }
  function smoothstep(t) { return t * t * (3 - 2 * t); }

  /* ===== Step stage (Neko's sticky runway, eased) =====
     One screen of stage plus 60% of a screen per step (CSS). One eased value p (0 to 1 over the runway) drives
     everything, so photos, step names, the gold line and the words can never drift apart. Each hand-over takes
     60% of a step's stretch, centred on the boundary between two steps: the next photo rises from 100% to 0 with a
     smoothstep, settling from 1.08 as it comes, while the one under it drifts up a fifth of its height and dims
     under a plum shade (parallax, so the stack reads as layers). The old words leave in the first half of the
     hand-over and the new ones arrive in the second, so two headlines never share the spot. The photos breathe
     from 1.02 to 1.08 across the whole runway. Transform and opacity only; layers are promoted only near the
     stage. Was: photos moved 1:1 with the raw scroll at about twice its pace, and the words swapped on a class
     toggle, which read as stepped. Reduced motion never adds .is-scrub: the static rows show instead. */
  (function () {
    var box = $('[data-stage]');
    if (!box || reduceMotion) return;
    box.classList.add('is-scrub');
    box.classList.add('is-lerp');
    var steps = $$('[data-sstep]', box);
    var names = $$('[data-sstep-name]', box);
    var panels = $$('[data-sstep-panel]', box);
    var imgs = panels.map(function (p) { return $('img', p); });
    var shades = panels.map(function (p) { return $('[data-sstep-shade]', p); });
    var bar = $('[data-stage-bar]', box);
    var N = steps.length, P = panels.length;
    var W = 0.6;  /* the hand-over's share of one step's stretch */
    var top = 0, run = 1, vh = 1, near = null, active = -1;
    function measure() {
      vh = window.innerHeight;
      top = box.getBoundingClientRect().top + window.pageYOffset;
      run = Math.max(1, box.offsetHeight - vh);
    }
    function isNear() { var y = window.pageYOffset; return y > top - vh * 1.5 && y < top + run + vh * 1.5; }
    function read() { return clamp((window.pageYOffset - top) / run, 0, 1); }
    function write(p) {
      var on = isNear();
      if (on !== near) {
        near = on;
        panels.forEach(function (el, k) {
          el.style.willChange = on ? 'transform' : '';
          if (imgs[k]) imgs[k].style.willChange = on ? 'transform' : '';
        });
      }
      var f = p * N, base = 1.02 + 0.06 * p, k, i;
      for (k = 0; k < P; k++) {
        var tin = k === 0 ? 1 : smoothstep(clamp((f - k + W / 2) / W, 0, 1));
        var tout = k + 1 < P ? smoothstep(clamp((f - k - 1 + W / 2) / W, 0, 1)) : 0;
        var ty = tin < 1 ? (1 - tin) * 100 : -20 * tout;
        panels[k].style.transform = 'translate3d(0,' + ty.toFixed(3) + '%,0)';
        panels[k].style.visibility = (tin <= 0 || tout >= 1) ? 'hidden' : '';
        if (imgs[k]) imgs[k].style.transform = 'scale(' + (base * (1 + 0.08 * (1 - tin))).toFixed(4) + ')';
        if (shades[k]) shades[k].style.opacity = (0.42 * tout).toFixed(3);
      }
      for (i = 0; i < N; i++) {
        var tIn = i === 0 ? 1 : smoothstep(clamp((f - i) / (W / 2), 0, 1));
        var tOut = i === N - 1 ? 0 : smoothstep(clamp((f - i - 1 + W / 2) / (W / 2), 0, 1));
        var o = tIn * (1 - tOut);
        steps[i].style.opacity = o.toFixed(3);
        steps[i].style.transform = 'translate3d(0,' + ((1 - tIn) * 24 - tOut * 16).toFixed(2) + 'px,0)';
        steps[i].style.visibility = o < 0.01 ? 'hidden' : 'visible';
      }
      if (bar) bar.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      var a = clamp(Math.floor(f), 0, N - 1);
      if (a !== active) {
        if (active > -1) {
          steps[active].classList.remove('is-active');
          if (names[active]) names[active].classList.remove('is-active');
        } else {
          steps.forEach(function (s) { s.classList.remove('is-active'); });
          names.forEach(function (n) { n.classList.remove('is-active'); });
        }
        active = a;
        steps[active].classList.add('is-active');
        if (names[active]) names[active].classList.add('is-active');
      }
    }
    var wasNear = false;
    var follow = follower(read, write, 0.16, function () { var j = !wasNear; wasNear = isNear(); return j; });
    measure();
    wasNear = isNear();
    follow.snap();
    window.addEventListener('scroll', follow.kick, { passive: true });
    window.addEventListener('resize', function () { measure(); follow.kick(); });
    if (window.ResizeObserver) new ResizeObserver(function () { measure(); follow.kick(); }).observe(document.body);
  })();

  /* ===== Category cover (banner kind 'cover'): load, then a quiet scroll link =====
     Load: waits for the display font (1.2s at most), then .is-in; CSS slides the two title lines in from opposite
     sides, settles the photo and brings in the line and the pill. Scroll (eased, as the stage; no pin): while the
     cover leaves, the lines drift apart sideways (3vw each at most) and the frame eases to 1.05, Neko's link
     between scroll and image kept small. Reduced motion: everything in place at once, nothing scrubs. */
  (function () {
    var cover = $('[data-cover]');
    if (!cover) return;
    if (reduceMotion) { cover.classList.add('is-in'); return; }
    var done = false;
    function go() { if (done) return; done = true; raf(function () { cover.classList.add('is-in'); }); }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(go).catch(go);
    setTimeout(go, 1200);
    var lines = $$('[data-cover-line]', cover);
    var dirs = lines.map(function (l) { return +l.getAttribute('data-cover-line'); });
    var frame = $('[data-cover-frame]', cover);
    var H = 1, W = 1, near = null;
    function measure() { H = Math.max(1, cover.offsetHeight); W = window.innerWidth; }
    function read() { return clamp(window.pageYOffset / H, 0, 1); }
    function write(q) {
      var on = q < 1;
      if (on !== near) {
        near = on;
        lines.forEach(function (l) { l.style.willChange = on ? 'transform' : ''; });
        frame.style.willChange = on ? 'transform' : '';
      }
      for (var i = 0; i < lines.length; i++) {
        lines[i].style.transform = q > 0 ? 'translate3d(' + (dirs[i] * 0.03 * W * q).toFixed(1) + 'px,0,0)' : '';
      }
      frame.style.transform = q > 0 ? 'scale(' + (1 + 0.05 * q).toFixed(4) + ')' : '';
    }
    var follow = follower(read, write, 0.12);
    measure();
    follow.snap();
    window.addEventListener('scroll', follow.kick, { passive: true });
    window.addEventListener('resize', function () { measure(); follow.kick(); });
  })();

  /* ===== Drawer accordion (Margaux at 390): one program open at a time, the rows slide down (grid rows, CSS) ===== */
  (function () {
    var triggers = Array.prototype.slice.call(document.querySelectorAll('[data-accordion-trigger]'));
    triggers.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var opening = btn.getAttribute('aria-expanded') !== 'true';
        triggers.forEach(function (other) {
          other.setAttribute('aria-expanded', 'false');
          document.getElementById(other.getAttribute('aria-controls')).classList.remove('is-open');
        });
        if (opening) {
          btn.setAttribute('aria-expanded', 'true');
          document.getElementById(btn.getAttribute('aria-controls')).classList.add('is-open');
        }
      });
    });
  })();

  /* ===== Sticky mobile CTA: up past 200px, away while the closing band or footer is on screen ===== */
  (function () {
    var pill = $('[data-sticky-cta]');
    if (!pill) return;
    var link = $('a', pill);
    var blocked = false;
    var seen = [];
    function update() {
      var show = window.pageYOffset > 200 && !blocked;
      pill.classList.toggle('is-visible', show);
      pill.setAttribute('aria-hidden', show ? 'false' : 'true');
      if (link) link.tabIndex = show ? 0 : -1;
    }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var i = seen.indexOf(en.target);
          if (en.isIntersecting && i < 0) seen.push(en.target);
          if (!en.isIntersecting && i > -1) seen.splice(i, 1);
        });
        blocked = seen.length > 0;
        update();
      });
      $$('[data-sticky-stop]').forEach(function (b) { io.observe(b); });
    }
    scrollJobs.push(update);
    update();
  })();

  /* ===== Cookie notice: Accept remembers the choice; any "Cookie settings" control brings it back ===== */
  (function () {
    var box = $('[data-cookie]');
    if (!box) return;
    var key = STORE + 'cookie-choice';
    var choice = null;
    try { choice = window.localStorage.getItem(key); } catch (e) {}
    /* phones: wait for the first scroll, so the notice never covers the hero's lead and button (critic round 1) */
    if (!choice) {
      if (window.matchMedia('(max-width: 640px)').matches && window.pageYOffset < 200) {
        scrollJobs.push(function () { if (window.pageYOffset > 200 && box.hidden && !choice) { box.hidden = false; choice = 'shown'; } });
      } else {
        box.hidden = false;
      }
    }
    $$('[data-cookie-accept]', box).forEach(function (b) {
      b.addEventListener('click', function () {
        try { window.localStorage.setItem(key, 'accepted'); } catch (e) {}
        box.hidden = true;
      });
    });
    $$('[data-cookie-open]').forEach(function (b) {
      b.addEventListener('click', function () {
        box.hidden = false;
        var first = $('button, a', box);
        if (first) first.focus();
      });
    });
  })();

  /* ===== Forms: inline errors, a status region that takes focus, no fake success =====
     Messages live in data-msg-* attributes on the form, so both languages share this block. A form reports
     success only when window.SITE_FORM_ENDPOINT answers OK; with no endpoint it shows the error line, which
     gives the support email. */
  (function () {
    $$('[data-form]').forEach(function (form) {
      var status = $('[data-form-status]', form);
      function msg(k) { return form.getAttribute('data-msg-' + k) || ''; }
      function setError(field, text) {
        var err = document.getElementById(field.id + '-error');
        if (text) field.setAttribute('aria-invalid', 'true'); else field.removeAttribute('aria-invalid');
        if (err) err.textContent = text;
      }
      function check(field) {
        var v = (field.value || '').trim();
        if (field.type === 'checkbox') {
          var okBox = !(field.required && !field.checked);
          setError(field, okBox ? '' : msg('required'));
          return okBox;
        }
        if (field.required && !v) { setError(field, msg('required')); return false; }
        if (v && field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) { setError(field, msg('email')); return false; }
        if (v && field.type === 'tel' && v.replace(/\D/g, '').replace(/^1/, '').length !== 10) { setError(field, msg('phone')); return false; }
        setError(field, '');
        return true;
      }
      var fields = $$('input, select, textarea', form).filter(function (f) { return f.type !== 'hidden' && f.type !== 'submit'; });
      fields.forEach(function (f) {
        f.addEventListener('blur', function () { if (f.getAttribute('aria-invalid') === 'true') check(f); });
      });
      function say(text) {
        if (!status) return;
        status.textContent = text;
        status.focus();
      }
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var bad = fields.filter(function (f) { return !check(f); });
        if (bad.length) { bad[0].focus(); return; }
        var endpoint = window.SITE_FORM_ENDPOINT;
        if (!endpoint || !window.fetch) { say(msg('error')); return; }
        var btn = $('[type="submit"]', form);
        if (btn) btn.disabled = true;
        say(msg('sending'));
        fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error('status ' + r.status);
            say(msg('success'));
            form.reset();
          })
          .catch(function () { say(msg('error')); })
          .then(function () { if (btn) btn.disabled = false; });
      });
    });
  })();

  /* ===== Quiz: one question per screen, records nothing (spec 2b) =====
     Screens are [data-quiz-screen] sections; answers carry data-go="<screen>". Back walks the history,
     Start again clears it, and each new screen's heading takes focus. */
  (function () {
    var quiz = $('[data-quiz]');
    if (!quiz) return;
    var screens = $$('[data-quiz-screen]', quiz);
    var bar = $('[data-quiz-bar]');
    var trail = [];
    function show(id) {
      var target = null;
      screens.forEach(function (s) {
        var on = s.getAttribute('data-quiz-screen') === id;
        s.hidden = !on;
        if (on) target = s;
      });
      if (!target) return;
      if (bar) bar.style.setProperty('--p', target.getAttribute('data-progress') || 0);
      var h = $('h1, h2', target);
      if (h && trail.length > 1) { h.tabIndex = -1; h.focus({ preventScroll: true }); }
      window.scrollTo(0, 0);
    }
    quiz.hidden = false;
    $$('[data-quiz-noscript]').forEach(function (n) { n.hidden = true; });
    $$('[data-go]', quiz).forEach(function (b) {
      b.addEventListener('click', function () { var id = b.getAttribute('data-go'); trail.push(id); show(id); });
    });
    $$('[data-quiz-back]', quiz).forEach(function (b) {
      b.addEventListener('click', function () {
        if (trail.length > 1) trail.pop();
        show(trail[trail.length - 1]);
      });
    });
    $$('[data-quiz-restart]', quiz).forEach(function (b) {
      b.addEventListener('click', function () { trail = ['intro', 'q1']; show('q1'); });
    });
    trail.push('intro');
    show('intro');
  })();
})();
