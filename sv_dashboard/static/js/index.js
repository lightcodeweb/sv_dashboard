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