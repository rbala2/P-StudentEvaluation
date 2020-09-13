// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});

$(document).ready(function() {
  $('#resultsSummaryDT').DataTable({
        "order": [[ 2, "desc" ]]
    });
});