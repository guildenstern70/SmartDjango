
function closeModal() {
    console.log("Closing modal");
    const myModal =
        new bootstrap.Modal(document.getElementById('insertCarModal'), { keyboard: false });
    myModal.hide();
}