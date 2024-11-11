import React from 'react';
import { Link } from 'react-router-dom';

function UserTicketsHome() {
  return (
    <div>
      <h1>User Tickets Home</h1>
      <p>Welcome to the User Tickets Home Page. Here you can view and manage your tickets.</p>
      
      {/* Link to create a new ticket */}
      <Link to="/user_ticket_create">
        Create New Ticket
      </Link>

    </div>
  );
}

export default UserTicketsHome;
