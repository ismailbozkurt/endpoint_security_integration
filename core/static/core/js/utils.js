function createInputSection(label, type, name, content = null) {
  if (type == "text") {
    return textInput(label, content, name);
  } else {
    return passwordInput(label, content, name);
  }
}

function passwordInput(label, content, name) {
  var outerDiv = document.createElement("div");
  outerDiv.classList.add("col-md-12");

  var innerDiv = document.createElement("div");
  innerDiv.classList.add("form-group");

  var inputDiv = document.createElement("div");
  inputDiv.classList.add("input-container");

  var labelEl = document.createElement("label");
  labelEl.setAttribute("for", "example-text-input");
  labelEl.classList.add("form-control-label");
  labelEl.innerText = label;

  var inputElement = document.createElement("input");
  inputElement.classList.add("form-control", "form-control-sm");
  inputElement.type = "password";
  inputElement.name = name;

  if (content) {
    inputElement.value = content;
  }
  inputFields.push(inputElement);

  var toggleButton = document.createElement("button");
  toggleButton.id = "togglePassword";
  toggleButton.classList.add("eye-icon");
  toggleButton.classList.add("input-eye");

  toggleButton.innerHTML = "&#128065;";
  toggleButton.addEventListener("click", () => toggleInput(inputElement));

  inputDiv.appendChild(inputElement);
  inputDiv.appendChild(toggleButton);
  innerDiv.appendChild(labelEl);
  innerDiv.appendChild(inputDiv);
  outerDiv.appendChild(innerDiv);

  return outerDiv;
}

function textInput(label, content, name) {
  var outerDiv = document.createElement("div");
  outerDiv.classList.add("col-md-12");

  var innerDiv = document.createElement("div");
  innerDiv.classList.add("form-group");

  var labelEl = document.createElement("label");
  labelEl.setAttribute("for", "example-text-input");
  labelEl.classList.add("form-control-label");
  labelEl.innerText = label;

  var input = document.createElement("input");
  input.classList.add("form-control", "form-control-sm");
  input.setAttribute("type", "text");
  input.name = name;

  if (content) {
    input.value = content;
  }
  inputFields.push(input);

  innerDiv.appendChild(labelEl);
  innerDiv.appendChild(input);
  outerDiv.appendChild(innerDiv);

  return outerDiv;
}

function createSubmitButton(integration) {
  var outerDiv = document.createElement("div");
  outerDiv.classList.add("col-md-12", "justify-content-center");

  var innerDiv = document.createElement("div");
  innerDiv.classList.add(
    "form-group",
    "d-flex",
    "align-items-center",
    "justify-content-center"
  );

  var btn = document.createElement("button");
  btn.classList.add("btn", "btn-primary", "btn-sm");
  if (integration) {
    btn.innerText = "Integrate";
    btn.addEventListener("click", onIntegrateProduct);
  } else {
    btn.innerText = "Deintegrate";
    btn.addEventListener("click", deintegrateProduct);
  }

  innerDiv.appendChild(btn);
  outerDiv.appendChild(innerDiv);
  return outerDiv;
}

function clearContent(contentEl) {
  while (contentEl.firstChild) {
    contentEl.removeChild(contentEl.firstChild);
  }
}

function onIntegrateProduct() {
  // alert(`Button'a tıklandı! ${selected_product}`);
  var keys = {};
  for (i of inputFields) {
    keys[i.name] = i.value;
  }
  // console.log(keys)
  integrateProduct(keys);
}

function toggleInput(el) {
  type = el.type;
  if (type == "text") {
    el.type = "password";
  } else {
    el.type = "text";
  }
}

function integrateProduct(keys) {
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(keys),
  };
  console.log("keys:", keys);
  fetch(`api/integration/${selected_product_code}`, requestOptions).then(
    (res) => {
      console.log(res);
      if (res.status == 201) {
        updateKeys(selected_product_code, keys);
        selectProduct(null, selected_product_code);
        udpateProductIcon(true);
      } else {
        // handle error display
      }
    }
  );
}

function deintegrateProduct(product_name) {
  const requestOptions = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  };

  fetch(`api/integration/${selected_product_code}`, requestOptions).then(
    (res) => {
      if (res.status == 204) {
        // deleted
        updateKeys(selected_product_code, null);
        selectProduct(null, selected_product_code);
        udpateProductIcon(false);
      } else {
        // handle error display
      }
    }
  );
}

function udpateProductIcon(integrated) {
  let icon = document.getElementById(`${selected_product_code}-icon`);
  if (!integrated) {
    icon.classList.remove("text-success");
    icon.classList.add("text-secondary");
  } else {
    icon.classList.remove("text-secondary");
    icon.classList.add("text-success");
  }
}
