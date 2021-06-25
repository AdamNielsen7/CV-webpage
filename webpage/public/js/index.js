//Collabsible Categories Event Listener
document.querySelectorAll(".collapseButton").forEach(button => {
    button.addEventListener('touchend', e=> {
        let content = e.target.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
});

