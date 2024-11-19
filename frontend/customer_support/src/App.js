import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserHome from './userPages/UserTicketsHome.jsx';
import TicketsCreate from './userPages/UserTicketsCreate.jsx';
import UserTicketsDetail from './userPages/UserTicketsDetail.jsx';
import AdminHome from './adminPages/AdminTicketsHome.jsx';
import AdminTicketsDetail from './adminPages/AdminTicketsDetail.jsx';
import MyChatBot from './chatbot/chatBot.jsx';

function App() {
  return (
    <div>
    <Router>
      <Routes>
        <Route path="/user_tickets" element={<UserHome />} />
        <Route path="/user_ticket_create" element={<TicketsCreate />} />
        <Route path="/user_ticket_detail" element={<UserTicketsDetail />} />
        <Route path="/admin_tickets" element={<AdminHome />} />
        <Route path="/admin_ticket_detail" element={<AdminTicketsDetail />} />
        <Route path="/chatbot" element={<MyChatBot />}/>
      </Routes>
    </Router>
    </div>
  );
}

export default App;
