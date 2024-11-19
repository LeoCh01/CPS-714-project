import React from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import { useNavigate } from "react-router-dom";
import "../index.css";
import MyChatBot from "../components/ChatBot";

function UserTicketsCreate() {
  const [priority, setPriority] = useState("");
  const [ticket_text, setTicketText] = useState("");
  const navigate = useNavigate();

  const changeTicketPriority = (e) => {
    setPriority(e.target.value);
  };

  const changeTicketText = (e) => {
    setTicketText(e.target.value);
  };

  const handleGoBack = () => {
    navigate(-1); // This tells React Router to go back to the previous page
  };

  const submitTicket = (e) => {
    e.preventDefault();

    //Ticket parameters to be sent to backend
    const ticket = { ticket_status: "open", priority, ticket_text };
    // Log the ticket object to see its contents
    console.log("Ticket Object:", ticket);

    fetch("http://127.0.0.1:8000/base/tickets/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(ticket),
    }).then(() => {
      console.log("Ticket has been successfully submitted!");
    });
  };

  return (
    <div className="ticket-container">
      Create a Ticket
      <div>
        <label>
          Priority:
          <input id="priority" type="text" value={priority} onChange={changeTicketPriority} />
        </label>
      </div>
      <div>
        <label>
          Description:
          <input id="ticket_text" type="text" value={ticket_text} onChange={changeTicketText} />
        </label>
      </div>
      <button type="submit" className="create-button" onClick={handleGoBack}>
        Back
      </button>
      <button className="create-button" onClick={submitTicket}>
        Submit
      </button>
      <MyChatBot />
    </div>
  );
}

export default UserTicketsCreate;
