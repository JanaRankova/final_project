
const handleEvent = (element, eventType, selector, handler) => {
    element.addEventListener(eventType, (event) => {
        const target = event.target.closest(selector)
        if (event.target && event.target.closest) {
            const target = event.target.closest(selector)

            if (target && element.contains(target)) {
                handler(event)
            }
        }
    })
}

const handleFlashButtonClick = (event => {
    const {target} = event
    const flashed = target.closest('.flashmessage')
    flashed.classList.add('dismissed')
})

handleEvent(document, 'click', '.flashmessage .dismiss', handleFlashButtonClick)


handleEvent(document, 'mouseover', '.star-rating', (event) => {
    const star = event.target
    const ratingValue = star.dataset.ratingValue
    const bookStars = star.closest('.star-rating-wrapper').querySelectorAll('.star-rating')

    bookStars.forEach((bookStar) => {
        if (bookStar.dataset.ratingValue <= ratingValue) {
            bookStar.classList.add('highlighted')
        } else {
            bookStar.classList.remove('highlighted')
        }
    })
    
})


const starRatingWrappers = document.querySelectorAll('.star-rating-wrapper')
starRatingWrappers.forEach((starRatingWrapper) => {
    handleEvent(starRatingWrapper, 'mouseleave', '.star-rating-wrapper', (event) => {
        const starsWithin = event.target.querySelectorAll('.star-rating')
        starsWithin.forEach((star) => {
            star.classList.remove('highlighted')
        })
    })
})


const show = (element) => {
    element.classList.remove('hidden')
}

const hide = (element) => {
    element.classList.add('hidden')
}


const filterList = (searchValue) => {
    const filter = searchValue.toLowerCase()

    const searchClear = document.getElementById('search-clear')
    const searchNores = document.getElementById('search-nores')
    const bookSearchTarget = document.querySelectorAll('.book-search-target')

    if (filter) {
        show(searchClear)
    } else {
        hide(searchClear)
    }

    bookSearchTarget.forEach((book) => {
        const name = book.dataset.name.toLowerCase()
        const authorName = book.dataset.author.toLowerCase()
        
        if (name.includes(filter) || authorName.includes(filter)){
            show(book)
        } else {
            hide(book)
        }
    })

    const hiddenBooks = document.querySelectorAll('.book-search-target.hidden')

    if (hiddenBooks.length === bookSearchTarget.length) {
        show(searchNores)
    } else {
        hide(searchNores)
    }
}

handleEvent(document, 'keyup', '#search-box', (event) => {
    filterList(event.target.value)
})

handleEvent(document, 'click', '#search-clear', (event) => {
    filterList('')
    const searchInput = document.getElementById('search-box')
    searchInput.value = ''
})
