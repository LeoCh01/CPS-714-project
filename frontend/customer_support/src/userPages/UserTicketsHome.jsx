import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TicketList.css';
import { useNavigate } from 'react-router-dom';

const Tickets = () => {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedTicket, setSelectedTicket] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/base/tickets/');
        setTickets(response.data);
      } catch (error) {
        setError('Error fetching tickets');
      } finally {
        setLoading(false);
      }
    };
    fetchTickets();
  }, []);

  if (loading) return <p>Loading tickets...</p>;
  if (error) return <p>{error}</p>;

  const handleCreateClick = () => {
    navigate('/user_ticket_create');
  };

  const handleTicketClick = (ticket) => {
    setSelectedTicket(ticket);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedTicket(null);
  };


  return (
    <div className="ticket-container">
      <button className="create-button" onClick={handleCreateClick}>Create</button>
      <h2>Tickets</h2>
      <div className="ticket-table">
        <div className="ticket-header">
          <span className="ticket-column">Title</span>
          <span className="ticket-column">Status</span>
          <span className="ticket-column">Date Created</span>
        </div>
        {tickets.map((ticket) => (
          <div
            className="ticket-row"
            key={ticket.ticket_id}
            onClick={() => handleTicketClick(ticket)}
          >
            <span className="ticket-column">Ticket - {ticket.ticket_id}</span>
            <span className="ticket-column">{ticket.priority}</span>
            <span className="ticket-column">{ticket.created_at}</span>
          </div>
        ))}
      </div>


      {isModalOpen && selectedTicket && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>Ticket #{selectedTicket.ticket_id}</h2>
            <p><strong>Priority:</strong> {selectedTicket.priority}</p>
            <p><strong>Date Created:</strong> {selectedTicket.created_at}</p>
            <p><strong>Description:</strong> {selectedTicket.ticket_text || 'No description available'}</p>
            <button onClick={handleCloseModal}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Tickets;
