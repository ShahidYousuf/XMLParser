$(document).ready(function() {
// Login Form JS


// detail view js
$("#detail-table").DataTable({
    "searching": true,
    "language": {
            "lengthMenu": "Show _MENU_ students per page",
            "zeroRecords": "No data found",
            "info": "Showing page _PAGE_ of _PAGES_",
            "infoEmpty": "No records available",
            "infoFiltered": "(filtered from _MAX_ total records)"
        }
});


});