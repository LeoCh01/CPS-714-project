import React from "react";
import { Link, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import BackButton from "../components/BackButton";
import "../userPages/defaultStyle.css";

function AdminTicketsDetail() {
  const { ticketId } = useParams();
  const [ticket, setTicket] = useState(null);
  const [ticketRes, setTicketRes] = useState(null);
  const [ticketResText, setTicketResText] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/base/tickets/${ticketId}/`)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((ticketData) => {
        setTicket(ticketData);
      })
      .catch((err) => {
        console.error("Error fetching: ", err.message);
      });
  }, [ticketId]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/base/tickets/response/${ticketId}`) //Ticket_id Foreign key needs to be implemented
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((ticketResData) => {
        setTicketRes(ticketResData);
        setTicketResText(ticketResData.response_text);
      })
      .catch((err) => {
        console.error("Error fetching: ", err.message);
      });
  }, []);

  const { ticket_id, ticket_status, priority, created_at, ticket_text, user_user } = ticket || {};
  //const ticket_response = ticketRes?.response_text || "No response yet";
  const ticket_user_res = ticketRes?.user_id || "No response yet";

  function handleChange(e) {
    setTicketResText(e.target.value);
  }

  const submitTicket = (e) => {
    //Make ticket_response_id=ticket_id?, add tickets_ticket, get user_id
    const ticketPost = {
      ticket_response_id: ticketId,
      user_id: "admin",
      response_text: ticketResText,
      responded_at: "2024-11-13",
    };

    fetch(`http://127.0.0.1:8000/base/tickets/response/create`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(ticketPost),
    }).then(() => {
      console.log("Ticket has been successfully submitted!");
    });

    fetch(`http://127.0.0.1:8000/base/tickets/update/${ticketId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ticket_status: "closed" }),
    }).then(() => {
      console.log("Ticket has been successfully updated!");
    });
  };

  return (
    <div className="ticket-container">
      <h1>Ticket - {ticket_id}</h1>

      <div className="ticket-table">
        <h2>Details</h2>

        <div>Status: {ticket_status}</div>
        <div>Priority: {priority}</div>
        <div>Created By: {user_user}</div>
        <div>Creation Date: {created_at}</div>
        <div>Response From: {ticket_user_res}</div>
      </div>

      <div>
        <label>
          <h2>Description</h2>
          <textarea value={ticket_text} readOnly={true} rows={10} cols={70} />
        </label>
      </div>

      <div>
        <label>
          <h2>Response</h2>
          <textarea value={ticketResText} onChange={handleChange} rows={10} cols={70} />
        </label>
      </div>

      <BackButton className="create-button" />

      <button className="create-button" onClick={submitTicket}>
        Submit
      </button>
    </div>
  );
}

export default AdminTicketsDetail;
