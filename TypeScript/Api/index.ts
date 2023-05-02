import API from "./api";

// Utilisation de la classe
const api = new API();

// create
api
  .create({ name: "John Doe", email: "johndoe@email.com" })
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));

// get
api
  .get(1)
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));

// update
api
  .update(1, { name: "Jane Doe", email: "janedoe@email.com" })
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));

// delete
api
  .delete(1)
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));
