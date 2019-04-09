---
layout: default
---

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>

  function check_valid(element) {
    if (element.value) {
      element.classList.add("is-valid")
      element.classList.remove("is-invalid")
    } else {
      element.classList.remove("is-valid")
      element.classList.add("is-invalid")
    }
  }

  function send() {

    var message = document.getElementById("message")
    var name = document.getElementById("name")
    var contact = document.getElementById("contact")
    var button = document.getElementById("button")
    var alert = document.getElementById("alert")

    check_valid(message)
    check_valid(name)
    check_valid(contact)

    if (message.value && name.value && contact.value) {

      button.disabled = true
      button.value = "Sending..."

      var url = "https://7xs0bfw3bh.execute-api.eu-west-1.amazonaws.com/prod/sms"
      var content = {"msg": message.value + "\n\n" + name.value + "\n" + contact.value}
      var option = {'headers': {'x-api-key': 'ZpDE86XzPsJGNcQ5FxBLCbkRYBxxGI683EsGpEa0'}}

      axios.post(url, content, option)
        .then((res) => {
          // console.log(res.data)

          if (res.data.status_code == 200) {

            button.classList.remove("btn-outline-dark")
            button.classList.add("btn-success")
            button.value = "Message sent succesfully !"

            message.disabled = true
            name.disabled = true
            contact.disabled = true

          } else {

            button.style.visibility = 'hidden';

            alert.classList.add("alert-danger")
            alert.innerHTML += "<p>SMS not sent :/</p>"
            alert.innerHTML += "<p>Error : " + res.data.status_code + " - " + res.data.status_message + "</p>"
            alert.innerHTML += '<input type="button" class="btn btn-outline-danger" id="alert-button" value="Try again" onclick="reset()">'
            alert.classList.remove("collapse")

          }

        })
        .catch((error) => {
          console.error(error);

          button.style.visibility = 'hidden';

          alert.classList.add("alert-danger")
          alert.innerHTML += "<p>Something went wrong :/</p>"
          alert.innerHTML += '<input type="button" class="btn btn-outline-dark" id="alert-button" value="Try again" onclick="reset()">'
          alert.classList.remove("collapse")

        });

    }
  }

  function close_alert() {
    var alert = document.getElementById("alert")
    alert.classList.add("collapse")
  }

  function reset() {
    var message = document.getElementById("message")
    var name = document.getElementById("name")
    var contact = document.getElementById("contact")
    var button = document.getElementById("button")
    var alert = document.getElementById("alert")

    message.classList.remove("is-valid")
    message.classList.remove("is-invalid")

    name.classList.remove("is-valid")
    name.classList.remove("is-invalid")

    contact.classList.remove("is-valid")
    contact.classList.remove("is-invalid")

    button.disabled = false
    button.classList.add("btn-outline-dark")
    button.classList.remove("btn-success")
    button.value = "Send to my phone"
    button.style.visibility = 'visible'

    alert.classList.add("collapse")
    alert.innerHTML = ""
  }

</script>

# Send me a SMS

<div class="form-group">
  <label>Message</label>
  <textarea class="form-control form-control-sm" id="message" placeholder="Tell me" maxlength="400"></textarea>
</div>
<div class="form-group">
  <div class="row">
    <div class="col">
      <label>Name</label>
      <input type="text" class="form-control form-control-sm" id="name" placeholder="Who are you?" maxlength="30">
    </div>
    <div class="col">
      <label>Your contact</label>
      <input type="text" class="form-control form-control-sm" id="contact" placeholder="Your email or phone number" maxlength="40">
    </div>
  </div>
</div>

<div class="alert alert-danger collapse" id="alert" role="alert"></div>

<input type="button" class="btn btn-outline-dark" id="button" value="Send to my phone" onclick="send()">
