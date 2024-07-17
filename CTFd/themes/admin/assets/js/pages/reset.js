import "./main";
import $ from "jquery";
import { ezQuery } from "../compat/ezq";

function reset(event) {
  event.preventDefault();
  ezQuery({
    title: "Reset CyberRange ?",
    body: "Are you sure you want to reset the CyberRange ?",
    success: function () {
      $("#reset-ctf-form").off("submit").submit();
    },
  });
}

$(() => {
  $("#reset-ctf-form").submit(reset);
});
