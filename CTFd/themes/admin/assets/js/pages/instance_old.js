import "./main";
import $ from "jquery";
import "../compat/json";
import "../compat/format";
import CTFd from "../compat/CTFd";
import { htmlEntities } from "@ctfdio/ctfd-js/utils/html";
import { ezQuery, ezBadge } from "../compat/ezq";
import { createGraph, updateGraph } from "../compat/graphs";
import Vue from "vue";
import CommentBox from "../components/comments/CommentBox.vue";

function createInstance(event) {

  event.preventDefault();
  const params = $("#instance-info-create-form").serializeJSON(true);

  /*
  params.fields = [];

  for (const property in params) {
    if (property.match(/fields\[\d+\]/)) {
      let field = {};
      let id = parseInt(property.slice(3, -1));
      field["field_id"] = id;
      field["value"] = params[property];
      params.fields.push(field);
      delete params[property];
    }
  }
  */

  // Move the notify value into a GET param
  let url = "/api/v1/users";
  let notify = params.notify;
  if (notify === true) {
    url = `${url}?notify=true`;
  }
  delete params.notify;


  CTFd.fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(params),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (response) {
      if (response.success) {
        const instance_id = 5;
        window.location = CTFd.config.urlRoot + "/admin"; //instances/" + instance_id;
      }
    });

}



$(() => {


  $("#instance-info-create-form").submit(createInstance);

});