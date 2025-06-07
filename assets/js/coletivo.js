
let isVisible = false;

const visibleDivs = (name) => {

    // who is chosen
    const names = ['thayna', 'pablo', 'fabio'];

    // para cada item de names
    names.map( (item) => {
        //selected elements
        const selected = document.querySelector(`#cv-body-${item}`);
        //the selected one fills the following condition;
        const isTarget = item === name;

        selected.style.display = isTarget && selected.style.display !== "block" ? "block" : "none";
    });

}
