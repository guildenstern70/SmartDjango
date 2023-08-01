
function closeModal() {
    console.log("Closing insert new modal");
    const myModal =
        new bootstrap.Modal(document.getElementById('insertCarModal'), { keyboard: false });
    myModal.hide();
}

function showDeleteModal(carId) {
    console.log("Delete modal for car #" + carId);
    const idLabel = document.getElementById('deleteCarId');
    idLabel.innerText = carId;
    const deleteHref = "delete/" + carId;
    document.getElementById("deleteLink").href = deleteHref;
    console.log("Delete link is " + deleteHref);
    const myModal =
        new bootstrap.Modal(document.getElementById('deleteCarModal'), { keyboard: false });
    myModal.show();
}