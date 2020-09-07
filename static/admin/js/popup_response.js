/*
 * SmartDjango Python Project
 *
 * Copyright (c) 2020 Alessio Saltarin
 * This software is distributed under MIT License.
 * See LICENSE.
 *
 */

/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();
