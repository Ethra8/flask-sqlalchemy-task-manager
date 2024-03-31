document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization - Materialize
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialization (add task form) - Materialize
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {
            done: "Select"
        }
    });

    // select initialization
    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

});