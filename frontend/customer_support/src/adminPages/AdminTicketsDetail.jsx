import React from "react";
import { Link } from "react-router-dom";
import BackButton from "../components/BackButton";

function AdminTicketsDetail() {
  return (
    <div>
      <h1>Ticket - </h1>

      <div>
        <h2>Details</h2>

        <div>Status: {}</div>
        <div>Feature: {}</div>
        <div>Created By: {}</div>
        <div>Creation Date: </div>
      </div>

      <div>
        <label>
          <h2>Description</h2>
          <textarea value={"sample text"} readOnly={true} rows={10} cols={25} />
        </label>
      </div>

      <div>
        <label>
          <h2>Response</h2>
          <textarea value={"sample text"} rows={10} cols={25} />
        </label>
      </div>

      <BackButton />
    </div>
  );
}

export default AdminTicketsDetail;
