var elems = document.querySelectorAll(".dtp");
var fecha = document.getElementById("fecha");
var fecha_final = document.getElementById("fecha_final");
var desde = document.getElementById("desde");
var hasta = document.getElementById("hasta");

elems.forEach(function (el) {
  var datepicker = new Datepicker(el, {
    language: "es",
    format: "dd M yyyy",
  });
  el.addEventListener("changeDate", function (e) {
    switch (e.target.id) {
      case "datepicker":
        fecha.value = e.detail.date.getTime() / 1000;
        break;
      case "datepicker2":
        fecha_final.value = e.detail.date.getTime() / 1000;
        break;
      case "desdep":
        desde.value = e.detail.date.getTime() / 1000;
        break;
      case "hastap":
        hasta.value = e.detail.date.getTime() / 1000;
        break;
      default:
    }
  });
});

var f = document.getElementById("busqueda-form");
if (f) {
  f.addEventListener("submit", function (e) {
    if (desde.value == "" && hasta.value != "") {
      alert("Ingresa la fecha inicial");
      desde.focus();
      e.preventDefault();
      return false;
    }

    if (desde.value != "" && hasta.value != "") {
      var desdeval = desde.value * 1;
      var hastaval = hasta.value * 1;
      if (hastaval < desdeval) {
        alert("Corrige el rango de fechas.");
        desde.focus();
        e.preventDefault();
        return false;
      }
    }
  });
}

var pdfLinks = document.querySelectorAll(".show-pdf");

pdfLinks.forEach(function (el) {
  el.addEventListener("click", function (e) {
    e.preventDefault();
    var myModal = new bootstrap.Modal(document.getElementById("commonModal"));
    var iframePDF = document.getElementById("iframepdf");
    iframePDF.src = e.target.href;
    myModal.show();
  });
});
