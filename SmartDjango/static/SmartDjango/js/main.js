/*
 * SmartDjango Python Project
 *
 * Copyright (c) 2021-26 Alessio Saltarin
 * This software is distributed under MIT License.
 * See LICENSE.
 *
 */

(function () {

    const currentPage = window.location.href;
    console.log(window.location.href);
    if (currentPage.indexOf("home") > 0) {
        setActivePageLink("home");
    } else if (currentPage.indexOf("cars") > 0) {
        setActivePageLink("cars");
    } else if (currentPage.indexOf("One") > 0) {
        setActivePageLink("one");
    } else {
        setActivePageLink("two")
    }

})();

function setActivePageLink(pageName) {
    const homelink = document.getElementById("homelink");
    const carslink = document.getElementById("carslink");
    const pageonelink = document.getElementById("pageonelink");
    const pagetwolink = document.getElementById("pagetwolink");

    switch (pageName) {
        case 'home':
            homelink.classList.add("active");
            carslink.classList.remove("active");
            pageonelink.classList.remove("active");
            pagetwolink.classList.remove("active");
            break;
        case 'cars':
            homelink.classList.remove("active");
            carslink.classList.add("active");
            pageonelink.classList.remove("active");
            pagetwolink.classList.remove("active");
            break;
        case 'one':
            homelink.classList.remove("active");
            carslink.classList.remove("active");
            pageonelink.classList.add("active");
            pagetwolink.classList.remove("active");
            break;
        case 'two':
            homelink.classList.remove("active");
            carslink.classList.remove("active");
            pageonelink.classList.remove("active");
            pagetwolink.classList.add("active");
            break;
        default:
            console.log(`Sorry, cannot recognize ${pageName}.`);
    }

}

// ── Theme toggle ──────────────────────────────────────────────────────────────

function _getCurrentTheme() {
    return document.documentElement.getAttribute('data-bs-theme') || 'dark';
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-bs-theme', theme);
    localStorage.setItem('sd-theme', theme);
    // Update color-scheme meta so browser UI (scrollbars, inputs) follows
    var meta = document.querySelector('meta[name="color-scheme"]');
    if (meta) meta.content = theme;
    _updateThemeIcon(theme);
}

function toggleTheme() {
    setTheme(_getCurrentTheme() === 'dark' ? 'light' : 'dark');
}

function _updateThemeIcon(theme) {
    var icon = document.getElementById('theme-icon');
    var btn  = document.getElementById('theme-toggle-btn');
    if (!icon) return;
    if (theme === 'dark') {
        icon.className     = 'bi bi-sun-fill';
        if (btn) btn.title = 'Switch to light mode';
    } else {
        icon.className     = 'bi bi-moon-fill';
        if (btn) btn.title = 'Switch to dark mode';
    }
}

// Sync icon on every page load (theme already applied by inline <head> script)
document.addEventListener('DOMContentLoaded', function () {
    _updateThemeIcon(_getCurrentTheme());
});

// Keep icon accurate if OS theme changes while page is open
// (only relevant when no user preference is saved)
if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        if (!localStorage.getItem('sd-theme')) {
            _updateThemeIcon(_getCurrentTheme());
        }
    });
}
