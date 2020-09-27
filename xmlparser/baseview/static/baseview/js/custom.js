$(document).ready(function() {
// Login Form JS


// detail view js
$("#detail-table").DataTable({
    "searching": true,
    "language": {
            "lengthMenu": "Show _MENU_ students per page",
            "zeroRecords": "No data found",
            "info": "Showing page _PAGE_ of _PAGES_",
            "infoEmpty": "No students available",
            "infoFiltered": "(filtered from _MAX_ total students)"
        },
    //dom: 'lBfrtip',
    dom: "<'container mx-0 px-0' <'row' <'col-md-4' l><'col-md-4 float-left' f><'col-md-4' B>>>" + "rt" + "<'container mx-0 px-0' <'row' <'col-md-4' i><'col-md-8' p>>>",
    buttons : {
        name: 'primary',
        buttons: [{'extend':'pdf', 'text':'<i class="fa fa-file-pdf-o text-danger"></i> PDF'},
                  {'extend':'excel', 'text':'<i class="fa fa-file-excel-o text-success"></i> Excel'},
                  {'extend':'copy', 'text':'<i class="fa fa-clipboard text-white"></i> Copy'},
                  {'extend':'print', 'text':'<i class="fa fa-print text-white"></i> Print'},
                   ]
    },
});


});