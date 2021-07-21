document.querySelectorAll("button.contentTitle").forEach(button => {
    button.addEventListener('click', function() {
        this.classList.toggle("expanded");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display ="none";
        }
        else {
            content.style.display = "block";
        }
    })
})

function displayAnime(show) {
    const list = document.getElementById("animeList");
    let entry = document.createElement("a");
    entry.target = "_blank";
    entry.href = show.link;
    let image = document.createElement("img");
    image.src = show.image;
    image.alt = show.title;
    entry.appendChild(image);
    list.appendChild(entry);
}

var kitsuUserID = 44855
async function getKitsuLibrary(kitsuUserID) {
    fetch('https://kitsu.io/api/edge/library-entries?filter[userId]=' + kitsuUserID)
    .then(response => response.json())
    .then(library => {
        library.data.forEach(entry => {
            fetch(entry.relationships.anime.links.related)
            .then(response => response.json())
            .then(anime => {
                const attributes = anime.data.attributes;
                const link = "https://kitsu.io/anime/" + attributes.slug;
                const show = {title: attributes.titles.en,
                            link: link,
                            image: attributes.posterImage.small}
                displayAnime(show);
            });
        })
    });
}

getKitsuLibrary(kitsuUserID)


