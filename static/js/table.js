$(document).ready(function() {
	var table = $('#ftcTable').DataTable({
    "sScrollX": "100%",
    "sScrollXInner": "110%",
    "sScrollY": "600px",
     "bScrollCollapse": true
  }




		);

new $.fn.dataTable.FixedHeader(table);
});