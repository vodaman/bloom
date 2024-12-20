function toggleFill(id) {
    const heart = document.getElementsByClassName("fa-heart")[id]
    if (heart.classList.contains("fa-regular") == true) {
        heart.classList.remove("fa-regular")
        heart.classList.add("fa-solid")
    } else {
        heart.classList.remove("fa-solid")
        heart.classList.add("fa-regular")
    }
}