var table;
window.onload = () => {
    Init();
}

function Init() {
    table = $('#tbl_listings').DataTable({
        responsive: true,
        fixedHeader: {
            header: true
        },
        autoWidth: false
    });

    $('#tbl_listings thead tr').clone().appendTo('#tbl_listings thead');
    $('#tbl_listings thead tr:eq(1) th').each(function(i) {
        const title = $(this).text();
        $(this).removeClass('sorting_asc sorting');
        $(this).html('<input type="text" class="form-control" placeholder="Search ' + title + '" />');

        $('input', this).on('keyup change', function() {
            if (table.column(i).search() !== this.value) {
                table.column(i).search(this.value).draw();
                $(this).focus();
            }
        });
    });


    $('.btn-export').click(() => {
        downloadCSV();
    });
    $('.event-title').selectpicker();
    $('.event-brand').selectpicker();
    $('.event-title').change(titleChanged);
    $('.event-brand').change(brandChanged);

    reloadTable();
}

function titleChanged() {
    reloadTable();
}

function brandChanged() {
    reloadTable();
}

function reloadTable() {
    table.clear().draw();

    $.ajax({
        url: '/get_listings',
        method: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({
            title: $('.event-title option:selected').val(),
            brand: $('.event-brand option:selected').val()
        }),
        success: (data) => {
            data = JSON.parse(data);

            if (data.success) {
                for (listing of data.listings) {
                    table.row.add([
                        listing.section,
                        listing.row,
                        listing.price,
                        listing.quantity,
                        listing.num
                    ]);
                }

                table.draw();
            }
        }
    });
}

function downloadCSV() {
    window.open('/get_csv', '_blank');
}