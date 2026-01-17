import { useEffect, useState } from "react";
import API from "../api/api";

export default function Orders() {
  const [orders, setOrders] = useState([]);

  const fetchOrders = async () => {
    const res = await API.get("http://localhost:8003/orders/");
    setOrders(res.data);
  };

  useEffect(() => { fetchOrders(); }, []);

  return (
    <div>
      <h2>Orders</h2>
      {orders.map(o => (
        <div key={o.id}>
          <p>Order ID: {o.id}</p>
          <p>Total: {o.total_amount}</p>
          <p>Status: {o.status}</p>
          <p>Items:</p>
          <ul>
            {o.items.map(item => (
              <li key={item.product_id}>{item.product_id} x {item.quantity}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
