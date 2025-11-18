import axios from "axios"

function createAxios() {
  const token = localStorage.getItem("token")

  return axios.create({
    baseURL: "https://todoo.5xcamp.us",
    headers: {
      Authorization: token,
    },
  })
}

export { createAxios }
