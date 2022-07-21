document.addEventListener("DOMContentLoaded", () => {
    const expandsMore = document.querySelectorAll("#expand-more")

    function expand() {
        const showContent = document.getElementById(this.dataset.target)

        if (showContent.classList.contains('expand-active')) {
            this.textContent = this.dataset.showtext
        } else {
            this.textContent = this.dataset.hidetext
        }
        showContent.classList.toggle('expand-active')
    }

    expandsMore.forEach(expandMore => {
        expandMore.addEventListener('click', expand)
    })

})