window.onload = () => {
    Init();
}

function Init() {
    var table = $('#tbl_corps').DataTable({
        responsive: true,
        fixedHeader: {
            header: true
        }
    });
    $('.btn-export').click(() => {
        downloadCSV();
    });
}

function downloadCSV() {
    window.open('/get_csv', '_blank');
}