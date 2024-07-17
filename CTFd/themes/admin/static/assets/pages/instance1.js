import {
    $ as e,
    V as y,
    C as c,
    O as u,
    u as d,
    y as g
} from "./main-D_lcMXdT.js";
import {
    c as m,
    u as p
} from "../graphs-DV-0EwZa.js";
import {
    C as v
} from "../CommentBox-B45_juxF.js";
import "../echarts.common-KFqNeB6w.js";


function b(n) {
    n.preventDefault();
    const s = e("#instance-info-create-form").serializeJSON(!0);
    let t = "/api/v1/instances";

    c.fetch(t, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(s)
    }).then(function(o) {
        return o.json()
    }).then(function(o) {
        if (o.success) {
            //const r = o.data.id;
            window.location = c.config.urlRoot + "/admin/instances"; // + r;
        }
    })
}

function sendRequest(url, id) {
    c.fetch(url, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: id })
    }).then(function(o) {
        return o.json()
    }).then(function(o) {
        if (o.success) {
            window.location = c.config.urlRoot + "/admin/instances";
        }
    })
}

function createInstance(event) {
    const button = event.currentTarget;
    const id = button.getAttribute('data-id');

    let url = "/api/v1/instances/create";

    sendRequest(url, id)
}

function deleteInstance(event) {
    const button = event.currentTarget;
    const id = button.getAttribute('data-id');

    let url = "/api/v1/instances/delete";
    sendRequest(url, id)
}

e(() => {

    e("#instance-info-create-form").submit(b);

    e("#creating").click(createInstance);
    e("#deleting").click(deleteInstance);
});