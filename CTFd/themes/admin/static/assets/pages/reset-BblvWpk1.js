import{$ as e,u as s}from"./main-D_lcMXdT.js";function r(t){t.preventDefault(),s({title:"Reset CyberRange ?",body:"Are you sure you want to reset the CyberRange ?",success:function(){e("#reset-ctf-form").off("submit").submit()}})}e(()=>{e("#reset-ctf-form").submit(r)});