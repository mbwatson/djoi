const citationTogglers = document.querySelectorAll('.publication__citation-toggler')
const citationDialog = document.querySelector('.citation-dialog')
const citationDialogTitle = document.querySelector('.citation-dialog__title')
const citationDialogText = document.querySelector('.citation-dialog__citation__text')
const dialogCloser = document.querySelector('.citation-dialog__close-button')
const dialogBackdrop = document.querySelector('.dialog-backdrop')
const citationDialogCopyButton = document.querySelector('.citation-dialog__citation__copy-button')

function hideCitationDialog() {
    document.body.classList.remove('citation-open')
}

function showCitationDialog(e) {
    e.preventDefault()
    const doi = e.target.dataset.doi
    const citationTitle = document.querySelector(`.title${doi}`).innerText
    const citationText = document.querySelector(`.text${doi}`).innerText
    citationDialogTitle.innerText = citationTitle
    citationDialogText.innerText = citationText
    document.body.classList.add('citation-open')
}

for (let toggler of citationTogglers) {
    toggler.addEventListener('click', showCitationDialog)
}

dialogCloser.addEventListener('click', hideCitationDialog)
dialogBackdrop.addEventListener('click', hideCitationDialog)
document.addEventListener('keypress', (e) => {
    console.log(e.keyCode)
    if (e.keyCode === 27) {
        hideCitationDialog()
    }
})

citationDialogCopyButton.addEventListener('click', (e) => {
    console.log('copy not yet implemented.')
})