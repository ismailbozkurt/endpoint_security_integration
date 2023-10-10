window.onload = function () {
  getProducts();
};

var content = document.getElementById("main-content");
var contentTitle = document.getElementById("content-title");
var selected_product = null;
var selected_product_code = null;

var inputFields = [];

const products = [];

function getProducts() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  fetch(`api/products/`, requestOptions)
    .then((res) => res.json())
    .then((data) => {
      for (p of data) products.push(p);
      console.log(products);
      selectProduct(null, products[0].name);
    });
}

function getProductFields(name) {
  for (let product of products) {
    if (product.name == name) {
      return {
        fields: product.fields,
        keys: product.keys,
        name: product.name,
        display: product.display,
      };
    }
  }
  return null;
}

function selectProduct(el, p_name) {
  while (inputFields.length) {
    inputFields.pop();
  }
  console.log(p_name);
  const { fields, keys, name, display } = getProductFields(p_name);
  selected_product_code = name;

  if (fields !== null) {
    clearContent(content);
    for (let field of fields) {
      let label = field.display;
      let type = field.type;
      let name = field.name;
      fill = null;
      if (keys !== null) {
        fill = keys[name];
      }
      content.appendChild(createInputSection(label, type, name, fill));
    }
    content.appendChild(createSubmitButton(keys == null));
  }
  contentTitle.innerText = display;
}

function updateKeys(productName, keys) {
  for (let product of products) {
    if (product.name == productName) {
      product.keys = keys
    }
  }
}