var recipes;
var fuse;

function setup() {
    fetch('./recipes.json')
    .then((response) => response.json())
    .then((json) => {
        generateTable(json);
        recipes = json;
        fuse = new Fuse(json, {
            useExtendedSearch: true,
            keys: ['recipe_name', 'category', 'ingredients', 'effects','effects_category','method']
        });
    });
}

window.onload = setup;

function generateTable(data) {
    var table = document.getElementById("recipes");
    rows = [];

    data.forEach((value, i) => {
        rows.push(templatingRow(
            i,
            value.recipe_name,
            templatingCategory(value.category),
            value.ingredients.map(templatingIngredient).join(''),
            value.effects.map(templatingEffect).join(''),
            value.steps
        )
    );});

    table.innerHTML = rows.join('');
}

function templatingCategory(category) {
    return `<span class="badge rounded-pill text-bg-primary">${category}</span>`
}

function templatingIngredient(ingredient) {
    return `<span class="badge rounded-pill text-bg-dark">${ingredient}</span>`
}

function templatingEffect(effect) {
    return `<span class="badge rounded-pill text-bg-success">${effect}</span>`
}

function templatingRow(id, recipe_name, type, ingredients, effects, steps) {
    return `<tr>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${id}" aria-expanded="false" aria-controls="collapse${id}"><strong>${recipe_name}</strong></button>
        </h2>
        <div class="accordion-collapse collapse" id="collapse${id}" data-bs-parent="#recipes">
            <div class="accordion-body">
            <div>
                <div class="attributes">${type}<span class="px-1">|</span>${ingredients}<span class="px-1">|</span>${effects}</div>
                <p>${steps}</p>
            </div>
            </div>
        </div>
    </div>
</tr>
`
}

function onCook() {
    const input = document.getElementById("floatingInput").value;
    const allBoxes = Array.from(document.querySelectorAll("input[type=checkbox]"));
    

    const checkedBoxes = allBoxes.filter((value) => value.checked);
    // const checkedValues = checkedBoxes.map((value) => `="${value.value}"`);
    const checkedValues = checkedBoxes.map((value) => `"'${value.value}"`); // Modified this line

    const checkedString = checkedValues.join('|');

    const query_string = input + '|' + checkedString;
    console.log(input + '|' + checkedString)
    console.log(query_string);

    console.log(fuse.search(query_string))
    result = fuse.search(query_string);
    if (checkedBoxes.length == 0 && input == "") {
        generateTable(recipes);
        return;
    }
    generateTable(result.map((value) => value.item));
}
