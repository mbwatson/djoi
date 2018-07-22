const citationTogglers = document.querySelectorAll('.citation__toggler')
const citationDialog = document.querySelector('.citation-dialog')
const citationDialogTitle = document.querySelector('.citation-dialog__title')
const citationDialogText = document.querySelector('.citation-dialog__text')
const dialogCloser = document.querySelector('.citation-dialog__close-button')
const dialogBackdrop = document.querySelector('.dialog-backdrop')

function hideCitationDialog() {
    document.body.classList.remove('citation-open')
}

function showCitationDialog(e) {
    e.preventDefault()
    console.log(e.target)
    let doi = e.target.dataset.doi
    let citationText = document.querySelector(`.doi${doi}`).innerText
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