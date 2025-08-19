/*
 * SmartDjango Python Project
 *
 * Copyright (c) 2021-25 Alessio Saltarin
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
