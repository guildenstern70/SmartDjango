/*
 * SmartDjango Python Project
 *
 * Copyright (c) 2020 Alessio Saltarin
 * This software is distributed under MIT License.
 * See LICENSE.
 *
 */

(function($) {
    'use strict';
    var fields = $('#django-admin-prepopulated-fields-constants').data('prepopulatedFields');
    $.each(fields, function(index, field) {
        $('.empty-form .form-row .field-' + field.name + ', .empty-form.form-row .field-' + field.name).addClass('prepopulated_field');
        $(field.id).data('dependency_list', field.dependency_list).prepopulate(
            field.dependency_ids, field.maxLength, field.allowUnicode
        );
    });
})(django.jQuery);
