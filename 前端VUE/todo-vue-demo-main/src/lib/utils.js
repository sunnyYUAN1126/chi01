import Toastify from "toastify-js"
import "toastify-js/src/toastify.css"

function appAlert(text) {
  Toastify({
    text: text,
    position: "center",
  }).showToast()
}

export { appAlert }
