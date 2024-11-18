import React from "react";
import { Link, useParams } from "react-router-dom";
import BackButton from "../components/BackButton";
import { useEffect, useState } from "react";
import "./defaultStyle.css";

function UserTicketsDetail() {
  const { ticketId } = useParams();
  const [ticket, setTicket] = useState(null);
  const [ticketRes, setTicketRes] = useState(null);

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
    fetch(`http://127.0.0.1:8000/base/tickets/response/${ticketId}/`) //Ticket_id Foreign key needs to be implemented
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((ticketResData) => {
        setTicketRes(ticketResData);
      })
      .catch((err) => {
        console.error("Error fetching: ", err.message);
      });
  }, []);

  const { ticket_id, ticket_status, priority, created_at, ticket_text, user_user } = ticket || {};
  const ticket_response = ticketRes?.response_text || "No response yet";
  const ticket_user_res = ticketRes?.user_id || "No response yet";

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
          <textarea value={ticket_response} readOnly={true} rows={10} cols={70} />
        </label>
      </div>

      <BackButton className="create-button" />
    </div>
  );
}

export default UserTicketsDetail;
