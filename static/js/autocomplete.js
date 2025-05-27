document.addEventListener("DOMContentLoaded", () => {
    const input = document.querySelector("input[name='city']");
    let cities = [];


    fetch("/static/data/russia-cities.json")
        .then(response => response.json())
        .then(data => {
            cities = data.map(c => c.name);
        });


    input.addEventListener("input", function () {
        const value = this.value.toLowerCase();
        closeList();

        if (!value) return;

        const list = document.createElement("div");
        list.setAttribute("id", this.id + "autocomplete-list");
        list.setAttribute("class", "autocomplete-items list-group");
        this.parentNode.appendChild(list);

        let count = 0;
        cities.forEach(city => {
            if (count >= 10) return;
            if (city.toLowerCase().startsWith(value)) {
                const item = document.createElement("div");
                item.innerHTML = "<strong>" + city.substr(0, value.length) + "</strong>" + city.substr(value.length);
                item.classList.add("list-group-item");
                item.addEventListener("click", () => {
                    input.value = city;
                    closeList();
                });
                list.appendChild(item);
                count++;
            }
        });
    });

    function closeList() {
        const items = document.querySelectorAll(".autocomplete-items");
        items.forEach(item => item.remove());
    }

    document.addEventListener("click", () => closeList());
});